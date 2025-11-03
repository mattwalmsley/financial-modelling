"""
Bloomberg API request builders and response parsers.

This module provides high-level abstractions for constructing Bloomberg API
requests and parsing responses into typed data structures.
"""

import logging
from datetime import date, datetime
from typing import Any

import blpapi
import pandas as pd

from bbg_data.core.enums import BloombergField, Periodicity, RequestType, ServiceType
from bbg_data.core.models import HistoricalDataPoint, ReferenceDataPoint
from bbg_data.core.session import BloombergSession

logger = logging.getLogger(__name__)


class RequestBuilder:
    """
    Builder for Bloomberg API requests.

    Provides a fluent interface for constructing type-safe Bloomberg requests.
    """

    def __init__(self, session: BloombergSession, service_type: ServiceType) -> None:
        """
        Initialize request builder.

        Args:
            session: Active Bloomberg session
            service_type: Service to use for requests
        """
        self.session = session
        self.service = session.get_service(service_type)

    def create_reference_request(
        self,
        securities: list[str],
        fields: list[BloombergField],
        overrides: dict[str, str] | None = None,
    ) -> blpapi.Request:
        """
        Create a reference data request.

        Args:
            securities: List of Bloomberg tickers
            fields: List of fields to request
            overrides: Optional dictionary of override fields and values

        Returns:
            Bloomberg request object
        """
        request = self.service.createRequest(RequestType.REFERENCE_DATA.value)

        for security in securities:
            request.append("securities", security)

        for field in fields:
            request.append("fields", field.value)

        # Add overrides if provided
        if overrides:
            overrides_element = request.getElement("overrides")
            for field_name, value in overrides.items():
                override = overrides_element.appendElement()
                override.setElement("fieldId", field_name)
                override.setElement("value", value)

        return request

    def create_historical_request(
        self,
        securities: list[str],
        fields: list[BloombergField],
        start_date: date | str,
        end_date: date | str,
        periodicity: Periodicity = Periodicity.DAILY,
    ) -> blpapi.Request:
        """
        Create a historical data request.

        Args:
            securities: List of Bloomberg tickers
            fields: List of fields to request
            start_date: Start date (inclusive)
            end_date: End date (inclusive)
            periodicity: Data frequency

        Returns:
            Bloomberg request object
        """
        request = self.service.createRequest(RequestType.HISTORICAL_DATA.value)

        for security in securities:
            request.append("securities", security)

        for field in fields:
            request.getElement("fields").appendValue(field.value)

        # Handle date formatting
        if isinstance(start_date, date):
            start_date = start_date.strftime("%Y%m%d")
        if isinstance(end_date, date):
            end_date = end_date.strftime("%Y%m%d")

        request.set("startDate", start_date)
        request.set("endDate", end_date)
        request.set("periodicitySelection", periodicity.value)

        return request


class ResponseParser:
    """
    Parser for Bloomberg API responses.

    Converts raw Bloomberg response messages into typed Python objects.
    """

    @staticmethod
    def parse_reference_data(event: blpapi.Event) -> list[ReferenceDataPoint]:
        """
        Parse reference data response.

        Args:
            event: Bloomberg event containing response

        Returns:
            List of reference data points
        """
        results: list[ReferenceDataPoint] = []

        for msg in event:
            if not msg.hasElement("securityData"):
                continue

            sec_data_array = msg.getElement("securityData")

            for i in range(sec_data_array.numValues()):
                sec_data = sec_data_array.getValueAsElement(i)
                security = sec_data.getElementAsString("security")

                data_point = ReferenceDataPoint(security=security)

                # Parse field data
                if sec_data.hasElement("fieldData"):
                    field_data = sec_data.getElement("fieldData")
                    data_point.fields = ResponseParser._parse_field_data(field_data)

                # Parse errors
                if sec_data.hasElement("securityError"):
                    error_info = sec_data.getElement("securityError")
                    error_msg = error_info.getElementAsString("message")
                    data_point.errors.append(error_msg)

                if sec_data.hasElement("fieldExceptions"):
                    exceptions = sec_data.getElement("fieldExceptions")
                    for j in range(exceptions.numValues()):
                        exc = exceptions.getValueAsElement(j)
                        field_id = exc.getElementAsString("fieldId")
                        error_info = exc.getElement("errorInfo")
                        error_msg = error_info.getElementAsString("message")
                        data_point.errors.append(f"{field_id}: {error_msg}")

                results.append(data_point)

        return results

    @staticmethod
    def parse_historical_data(event: blpapi.Event) -> list[HistoricalDataPoint]:
        """
        Parse historical data response.

        Args:
            event: Bloomberg event containing response

        Returns:
            List of historical data points
        """
        results: list[HistoricalDataPoint] = []

        for msg in event:
            if not msg.hasElement("securityData"):
                continue

            sec_data = msg.getElement("securityData")
            security = sec_data.getElementAsString("security")

            if not sec_data.hasElement("fieldData"):
                continue

            field_data_array = sec_data.getElement("fieldData")

            for i in range(field_data_array.numValues()):
                field_data = field_data_array.getValueAsElement(i)

                # Extract date
                dt = field_data.getElementAsDatetime("date")
                data_date = dt.date() if isinstance(dt, datetime) else dt

                # Extract field values
                fields = ResponseParser._parse_field_data(field_data, exclude=["date"])

                data_point = HistoricalDataPoint(security=security, date=data_date, fields=fields)
                results.append(data_point)

        return results

    @staticmethod
    def _parse_field_data(
        element: blpapi.Element,
        exclude: list[str] | None = None,
    ) -> dict[str, Any]:
        """
        Parse field data from a Bloomberg element.

        Args:
            element: Bloomberg element containing field data
            exclude: List of field names to exclude

        Returns:
            Dictionary of field name to value
        """
        exclude = exclude or []
        fields: dict[str, Any] = {}

        for i in range(element.numElements()):
            field_element = element.getElement(i)
            field_name = str(field_element.name())

            if field_name in exclude:
                continue

            # Handle different data types
            try:
                if field_element.isArray():
                    # Array field - extract as list
                    values = []
                    for j in range(field_element.numValues()):
                        values.append(ResponseParser._extract_value(field_element, j))
                    fields[field_name] = values
                else:
                    # Scalar field
                    fields[field_name] = ResponseParser._extract_value(field_element)
            except Exception as e:
                logger.warning(f"Failed to parse field {field_name}: {e}")
                fields[field_name] = None

        return fields

    @staticmethod
    def _extract_value(element: blpapi.Element, index: int | None = None) -> Any:
        """
        Extract value from Bloomberg element with type handling.

        Args:
            element: Bloomberg element
            index: Index for array elements

        Returns:
            Extracted value with appropriate Python type
        """
        try:
            if index is not None:
                # Array element
                if element.isNull(index):
                    return None

                datatype = element.getValueAsElement(index).datatype()
                if datatype == blpapi.DataType.STRING:
                    return element.getValueAsString(index)
                elif datatype == blpapi.DataType.FLOAT64:
                    return element.getValueAsFloat(index)
                elif datatype == blpapi.DataType.INT32 or datatype == blpapi.DataType.INT64:
                    return element.getValueAsInteger(index)
                elif datatype == blpapi.DataType.DATE or datatype == blpapi.DataType.DATETIME:
                    return element.getValueAsDatetime(index)
                else:
                    return str(element.getValue(index))
            else:
                # Scalar element
                if element.isNull():
                    return None

                datatype = element.datatype()
                if datatype == blpapi.DataType.STRING:
                    return element.getValueAsString()
                elif datatype == blpapi.DataType.FLOAT64:
                    return element.getValueAsFloat()
                elif datatype == blpapi.DataType.INT32 or datatype == blpapi.DataType.INT64:
                    return element.getValueAsInteger()
                elif datatype == blpapi.DataType.DATE or datatype == blpapi.DataType.DATETIME:
                    dt = element.getValueAsDatetime()
                    return dt.date() if isinstance(dt, datetime) else dt
                else:
                    return str(element.getValue())
        except Exception:
            return None


def to_dataframe(data_points: list[HistoricalDataPoint | ReferenceDataPoint]) -> pd.DataFrame:
    """
    Convert data points to a pandas DataFrame.

    Args:
        data_points: List of historical or reference data points

    Returns:
        DataFrame with security and fields as columns
    """
    if not data_points:
        return pd.DataFrame()

    records = []
    for point in data_points:
        record = {"security": point.security}

        if isinstance(point, HistoricalDataPoint):
            record["date"] = point.date

        record.update(point.fields)
        records.append(record)

    return pd.DataFrame(records)
