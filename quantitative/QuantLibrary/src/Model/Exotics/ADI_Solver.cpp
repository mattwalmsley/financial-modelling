
#include <algorithm>
#include <Exotics/ADI_Solver.h>


ADISolver::ADISolver(const Grid2D& grid_,
                     const HestonParams& params_,
                     double K_, double B_, double T_, int Nt_)
    : grid(grid_), pde(params_), params(params_),
      K(K_), B(B_), T(T_), Nt(Nt_), dt(T_ / Nt_) {
    V.resize(grid.Nx, std::vector<double>(grid.Nv));
    initialize_payoff();
}

void ADISolver::initialize_payoff() {
    for (int i = 0; i < grid.Nx; ++i) {
        for (int j = 0; j < grid.Nv; ++j) {
            V[i][j] = (grid.S[i] > B) ? std::max(grid.S[i] - K, 0.0) : 0.0;
        }
    }
}

void ADISolver::apply_boundary_conditions() {
    for (int j = 0; j < grid.Nv; ++j)
        V[0][j] = 0.0; // absorbing barrier
}

void ADISolver::step_backwards() {
    std::vector<double> a(grid.Nx), b(grid.Nx), c(grid.Nx), d(grid.Nx), x(grid.Nx);

    for (int n = 0; n < Nt; ++n) {
        for (int j = 1; j < grid.Nv - 1; ++j) {
            for (int i = 1; i < grid.Nx - 1; ++i) {
                double dS, dV, dSS, dVV, dSV, rTerm;
                pde.coefficients(grid.S[i], grid.v[j], dS, dV, dSS, dVV, dSV, rTerm);

                double dx = grid.dS(i);
                double dx2 = dx * dx;

                a[i] = -0.5 * dt * (dSS / dx2 - dS / (2 * dx));
                b[i] = 1.0 + dt * (dSS / dx2 - rTerm);
                c[i] = -0.5 * dt * (dSS / dx2 + dS / (2 * dx));

                d[i] = V[i][j];
            }

            solve_tridiagonal(a, b, c, d, x);

            for (int i = 1; i < grid.Nx - 1; ++i) {
                V[i][j] = x[i];
            }
        }
        apply_boundary_conditions();
    }
}

double ADISolver::interpolate(double S0) const {
    auto it = std::lower_bound(grid.S.begin(), grid.S.end(), S0);
    int i = std::clamp(static_cast<int>(it - grid.S.begin()), 1, grid.Nx - 2);
    double w = (S0 - grid.S[i-1]) / (grid.S[i] - grid.S[i-1]);
    int j = std::clamp(static_cast<int>(params.v0 * (grid.Nv - 1)), 0, grid.Nv - 2);
    return (1 - w) * V[i-1][j] + w * V[i][j];
}

double ADISolver::price_down_and_out_call(double S0) {
    step_backwards();
    return interpolate(S0);
}

void ADISolver::solve_tridiagonal(const std::vector<double>& a,
                                  const std::vector<double>& b,
                                  const std::vector<double>& c,
                                  const std::vector<double>& d,
                                  std::vector<double>& x) {
    int n = b.size();
    std::vector<double> c_prime(n, 0.0);
    std::vector<double> d_prime(n, 0.0);

    c_prime[0] = c[0] / b[0];
    d_prime[0] = d[0] / b[0];

    for (int i = 1; i < n; ++i) {
        double denom = b[i] - a[i] * c_prime[i - 1];
        c_prime[i] = c[i] / denom;
        d_prime[i] = (d[i] - a[i] * d_prime[i - 1]) / denom;
    }

    x[n - 1] = d_prime[n - 1];
    for (int i = n - 2; i >= 0; --i) {
        x[i] = d_prime[i] - c_prime[i] * x[i + 1];
    }
}
