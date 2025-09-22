import heston_pde

params = heston_pde.HestonParams()
params.kappa = 2.0
params.theta = 0.04
params.sigma = 0.3
params.rho = -0.7
params.v0 = 0.04
params.r = 0.05

price = heston_pde.heston_barrier_option_price(
    S0=100, K=100, B=90, T=1.0,
    hp=params,
    Nx=100, Nv=50, Nt=100
)

print(f"Option price: {price:.4f}")
