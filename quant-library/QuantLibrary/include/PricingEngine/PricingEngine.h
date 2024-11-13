#pragma once

#include "Model/PricingModel.h"
#include "Instrument/Option.h"

class PricingEngine {
public:
    PricingEngine(PricingModel* model) : model(model) {}

    double priceOption(const Option& option) const {
        return model->calculatePrice(option);
    }

private:
    PricingModel* model;
};
