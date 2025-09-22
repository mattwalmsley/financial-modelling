#pragma once
#include <vector>

class Grid2D {
public:
    std::vector<double> S, v;
    int Nx, Nv;

    Grid2D(double S_min, double S_max, int Nx_,
           double v_min, double v_max, int Nv_);

    double dS(int i) const;
    double dv(int j) const;
};
