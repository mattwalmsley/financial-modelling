#include "Exotics/Heston_PDE.h"

void HestonPDE::coefficients(double S, double v, double& dS, double& dV,
                             double& dSS, double& dVV, double& dSV, double& rTerm) {
    dS  = params.r * S;
    dV  = params.kappa * (params.theta - v);
    dSS = 0.5 * v * S * S;
    dVV = 0.5 * params.sigma * params.sigma * v;
    dSV = params.rho * params.sigma * v * S;
    rTerm = -params.r;
}