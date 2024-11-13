#pragma once

#include "Instrument/Option.h"

class PricingModel {
public:
    virtual ~PricingModel() = default;
    virtual double calculatePrice(const Option& option) const = 0;
};
