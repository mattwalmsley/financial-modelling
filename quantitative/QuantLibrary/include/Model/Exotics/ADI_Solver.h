#pragma once

#include "Grid2D.h"
#include "HestonParams.h"
#include "Heston_PDE.h"
#include <vector>

class ADISolver {
public:
    ADISolver(const Grid2D& grid,
              const HestonParams& params,
              double K, double B, double T, int Nt);

    double price_down_and_out_call(double S0);

private:
    Grid2D grid;
    HestonPDE pde;
    HestonParams params;
    double K, B, T;
    int Nt;
    double dt;

    std::vector<std::vector<double>> V;

    void initialize_payoff();
    void apply_boundary_conditions();
    void step_backwards();
    void solve_tridiagonal(const std::vector<double>& a,
                           const std::vector<double>& b,
                           const std::vector<double>& c,
                           const std::vector<double>& d,
                           std::vector<double>& x);
    double interpolate(double S0) const;
};