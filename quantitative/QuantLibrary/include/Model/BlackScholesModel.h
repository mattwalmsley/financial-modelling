#pragma once

#include "PricingModel.h"
#include "Instrument/Option.h"
#include <cmath>

class BlackScholesModel : public PricingModel {
public:
    double calculatePrice(const Option& option) const override {
        double S = option.getUnderlyingPrice(); // Underlying asset price
        double K = option.getStrikePrice();     // Strike price
        double T = option.getExpirationTime();  // Time to expiration
        double r = 0.05;                        // Risk-free interest rate
        double sigma = 0.2;                     // Volatility

        // Black-Scholes formula
        double d1 = (std::log(S / K) + (r + 0.5 * sigma * sigma) * T) / (sigma * std::sqrt(T));
        double d2 = d1 - sigma * std::sqrt(T);

        double N_d1 = 0.5 * (1.0 + std::erf(d1 / std::sqrt(2.0)));
        double N_d2 = 0.5 * (1.0 + std::erf(d2 / std::sqrt(2.0)));

        return S * N_d1 - K * std::exp(-r * T) * N_d2;
    }
};
