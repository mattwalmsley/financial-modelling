#pragma once
#include <algorithm>

inline double call_payoff(double S, double K) {
    return std::max(S - K, 0.0);
}

