#include "Exotics/Grid2D.h"
#include <cmath>

Grid2D::Grid2D(double S_min, double S_max, int Nx_,
               double v_min, double v_max, int Nv_) : Nx(Nx_), Nv(Nv_) {
    S.resize(Nx);
    v.resize(Nv);

    // Tanh spacing around center
    for (int i = 0; i < Nx; ++i) {
        double x = -1.0 + 2.0 * i / (Nx - 1.0);
        S[i] = 0.5 * (S_min + S_max + (S_max - S_min) * std::tanh(2.5 * x));
    }

    for (int j = 0; j < Nv; ++j) {
        double x = -1.0 + 2.0 * j / (Nv - 1.0);
        v[j] = 0.5 * (v_min + v_max + (v_max - v_min) * std::tanh(2.0 * x));
    }
}

double Grid2D::dS(int i) const {
    if (i == 0) return S[1] - S[0];
    if (i == Nx - 1) return S[Nx - 1] - S[Nx - 2];
    return 0.5 * (S[i+1] - S[i-1]);
}

double Grid2D::dv(int j) const {
    if (j == 0) return v[1] - v[0];
    if (j == Nv - 1) return v[Nv - 1] - v[Nv - 2];
    return 0.5 * (v[j+1] - v[j-1]);
}
