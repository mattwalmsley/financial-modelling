#pragma once

#include "PricingEngine/PricingEngine.h"
#include "Instrument/Option.h"

class RiskEngine {
public:
    RiskEngine(PricingEngine* pricingEngine) : pricingEngine(pricingEngine) {}

    double calculateDelta(const Option& option) {
        // Example of a basic delta calculation
        double priceUp = pricingEngine->priceOption(option); // Price for a small increase in price
        Option optionUp(option.getStrikePrice(), option.getExpirationTime(), option.getUnderlyingPrice() + 0.01);
        double priceDown = pricingEngine->priceOption(optionUp); // Price for a small decrease in price
        return (priceUp - priceDown) / 0.01;
    }

private:
    PricingEngine* pricingEngine;
};
