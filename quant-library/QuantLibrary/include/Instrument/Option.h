#pragma once

#include "Instrument.h"

class Option : public Instrument {
public:
    Option(double strikePrice, double expirationTime, double underlyingPrice)
        : strikePrice(strikePrice), expirationTime(expirationTime), underlyingPrice(underlyingPrice) {}

    double getStrikePrice() const { return strikePrice; }
    double getExpirationTime() const { return expirationTime; }
    double getUnderlyingPrice() const { return underlyingPrice; }

    std::string getType() const override { return "Option"; }

private:
    double strikePrice;
    double expirationTime;
    double underlyingPrice;
};
