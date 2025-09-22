#include <pybind11/pybind11.h>
#include "Instrument/Option.h"
#include "Model/BlackScholesModel.h"
#include "PricingEngine/PricingEngine.h"
#include "RiskEngine/RiskEngine.h"
#include "Model/Exotics/HestonParams.h"
#include "Model/Exotics/Grid2D.h"
#include "Model/Exotics/ADI_Solver.h"
#include "Model/Exotics/Payoff.h"

namespace py = pybind11;

PYBIND11_MODULE(pyquantlibrary, m) {
    // Expose Option class to Python
    py::class_<Option>(m, "Option")
        .def(py::init<double, double, double>())  // Constructor
        .def("getStrikePrice", &Option::getStrikePrice)
        .def("getExpirationTime", &Option::getExpirationTime)
        .def("getUnderlyingPrice", &Option::getUnderlyingPrice);

    // Expose BlackScholesModel class to Python
    py::class_<BlackScholesModel>(m, "BlackScholesModel")
        .def("calculatePrice", &BlackScholesModel::calculatePrice);

    // Expose PricingEngine class to Python
    py::class_<PricingEngine>(m, "PricingEngine")
        .def(py::init<PricingModel*>())  // Constructor
        .def("priceOption", &PricingEngine::priceOption);

    // Expose RiskEngine class to Python
    py::class_<RiskEngine>(m, "RiskEngine")
        .def(py::init<PricingEngine*>())  // Constructor
        .def("calculateDelta", &RiskEngine::calculateDelta);

    // Expose HestonParams class to Python
    py::class_<HestonParams>(m, "HestonParams")
        .def_readwrite("kappa", &HestonParams::kappa)
        .def_readwrite("theta", &HestonParams::theta)
        .def_readwrite("sigma", &HestonParams::sigma)
        .def_readwrite("rho", &HestonParams::rho)
        .def_readwrite("v0", &HestonParams::v0)
        .def_readwrite("r", &HestonParams::r);

    // Expose Grid2D class to Python
    py::class_<Grid2D>(m, "Grid2D")
        .def(py::init<double, double, int, double, double, int>())  // Constructor
        .def_readonly("S", &Grid2D::S)
        .def_readonly("v", &Grid2D::v)
        .def_readonly("Nx", &Grid2D::Nx)
        .def_readonly("Nv", &Grid2D::Nv);

    // Expose ADISolver class to Python
    py::class_<ADISolver>(m, "ADISolver")
        .def(py::init<const Grid2D&, const HestonParams&, double, double, double, int>())  // Constructor
        .def("price_down_and_out_call", &ADISolver::price_down_and_out_call);
}
