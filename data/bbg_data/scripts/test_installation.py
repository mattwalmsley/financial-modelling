#!/usr/bin/env python3
"""
Quick start script to test bbg_data installation.

Run this script to verify that bbg_data is properly installed and
can connect to Bloomberg API.
"""

import sys


def test_import():
    """Test that the package can be imported."""
    print("Testing package import...")
    try:
        import bbg_data

        print(f"✓ Successfully imported bbg_data version {bbg_data.__version__}")
        return True
    except ImportError as e:
        print(f"✗ Failed to import bbg_data: {e}")
        return False


def test_connection():
    """Test connection to Bloomberg API."""
    print("\nTesting Bloomberg API connection...")
    try:
        from bbg_data import session
        from bbg_data.enums import ServiceType

        with session() as bbg:
            print("✓ Successfully connected to Bloomberg API")

            # Try to open reference data service
            service = bbg.get_service(ServiceType.REFDATA)
            print("✓ Successfully opened reference data service")

            return True

    except Exception as e:
        print(f"✗ Failed to connect to Bloomberg API: {e}")
        print("\nTroubleshooting:")
        print("  1. Ensure Bloomberg Terminal is running")
        print("  2. Check that you're logged into Bloomberg")
        print("  3. Verify API permissions are enabled")
        return False


def test_simple_query():
    """Test a simple data query."""
    print("\nTesting simple data query...")
    try:
        from bbg_data import session
        from bbg_data.enums import BloombergField, ServiceType
        from bbg_data.requests import RequestBuilder, ResponseParser

        with session() as bbg:
            builder = RequestBuilder(bbg, ServiceType.REFDATA)

            # Simple query for NVDA last price
            request = builder.create_reference_request(
                securities=["NVDA US Equity"], fields=[BloombergField.PX_LAST]
            )

            bbg.send_request(request)

            while True:
                event = bbg.next_event()
                data = ResponseParser.parse_reference_data(event)

                if data:
                    for point in data:
                        price = point.get_field(BloombergField.PX_LAST)
                        print(f"✓ NVDA last price: ${price}")

                if event.eventType() == 3:  # RESPONSE event
                    break

            return True

    except Exception as e:
        print(f"✗ Query failed: {e}")
        return False


def main():
    """Run all tests."""
    print("=" * 60)
    print("bbg_data Package Test Suite")
    print("=" * 60)

    results = []

    # Test 1: Import
    results.append(("Import", test_import()))

    if not results[-1][1]:
        print("\n⚠ Cannot proceed with further tests without successful import")
        sys.exit(1)

    # Test 2: Connection
    results.append(("Connection", test_connection()))

    if not results[-1][1]:
        print("\n⚠ Cannot test queries without Bloomberg connection")
    else:
        # Test 3: Simple query
        results.append(("Simple Query", test_simple_query()))

    # Summary
    print("\n" + "=" * 60)
    print("Test Summary")
    print("=" * 60)

    for test_name, passed in results:
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"{status}: {test_name}")

    all_passed = all(result[1] for result in results)

    if all_passed:
        print("\n🎉 All tests passed! Your installation is working correctly.")
        print("\nNext steps:")
        print("  1. Read the README.md for usage examples")
        print("  2. Try the examples in the examples/ directory")
        print("  3. Check out the CLI with: bbg-data --help")
    else:
        print("\n⚠ Some tests failed. Please review the errors above.")
        sys.exit(1)


if __name__ == "__main__":
    main()
