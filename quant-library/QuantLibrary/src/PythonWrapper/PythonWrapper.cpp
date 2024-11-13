#include <boost/python.hpp>
#include "Instrument/Option.h"
#include "Model/BlackScholesModel.h"
#include "PricingEngine/PricingEngine.h"
#include "RiskEngine/RiskEngine.h"

using namespace boost::python;

BOOST_PYTHON_MODULE(pyquantlibrary) {
    // Expose Option class to Python
    class_<Option>("Option", init<double, double, double>())
        .def("getStrikePrice", &Option::getStrikePrice)
        .def("getExpirationTime", &Option::getExpirationTime)
        .def("getUnderlyingPrice", &Option::getUnderlyingPrice);

    // Expose BlackScholesModel class to Python
    class_<BlackScholesModel, boost::noncopyable>("BlackScholesModel")
        .def("calculatePrice", &BlackScholesModel::calculatePrice);

    // Expose PricingEngine class to Python
    class_<PricingEngine>("PricingEngine", init<PricingModel*>())
        .def("priceOption", &PricingEngine::priceOption);

    // Expose RiskEngine class to Python
    class_<RiskEngine>("RiskEngine", init<PricingEngine*>())
        .def("calculateDelta", &RiskEngine::calculateDelta);
}
