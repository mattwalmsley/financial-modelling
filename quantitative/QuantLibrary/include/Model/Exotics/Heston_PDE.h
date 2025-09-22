#pragma once
#include "HestonParams.h"

class HestonPDE {
public:
    HestonPDE(const HestonParams& p) : params(p) {}

    void coefficients(double S, double v, double& dS, double& dV,
                      double& dSS, double& dVV, double& dSV, double& rTerm);

private:
    HestonParams params;
};
