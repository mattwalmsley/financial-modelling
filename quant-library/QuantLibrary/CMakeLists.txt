cmake_minimum_required(VERSION 3.10)
project(QuantLibrary VERSION 0.1.0)

# Enable testing
include(CTest)
enable_testing()

# Ensure Python and Boost are found before continuing
find_package(Python3 REQUIRED COMPONENTS Interpreter Development)
if(NOT Python3_FOUND)
    message(FATAL_ERROR "Python3 not found")
endif()

find_package(Boost REQUIRED COMPONENTS python)
if(NOT Boost_FOUND)
    message(FATAL_ERROR "Boost not found")
endif()

# Create the libraries
set(MODEL_SOURCES
        src/Model/BlackScholesModel.cpp
        src/Model/PricingModel.cpp
)

set(PRICING_ENGINE_SOURCES
        src/PricingEngine/PricingEngine.cpp
)

set(RISK_ENGINE_SOURCES
        src/RiskEngine/RiskEngine.cpp
)

set(PYTHON_WRAPPER_SOURCES
        src/PythonWrapper/PythonWrapper.cpp
)

add_library(model ${MODEL_SOURCES})
target_include_directories(model PUBLIC ${CMAKE_SOURCE_DIR}/include/Model)

add_library(pricing_engine ${PRICING_ENGINE_SOURCES})
target_include_directories(pricing_engine PUBLIC ${CMAKE_SOURCE_DIR}/include/PricingEngine)

add_library(risk_engine ${RISK_ENGINE_SOURCES})
target_include_directories(risk_engine PUBLIC ${CMAKE_SOURCE_DIR}/include/RiskEngine)

# Setup pyquantlibrary
add_library(pyquantlibrary SHARED ${PYTHON_WRAPPER_SOURCES})
target_include_directories(pyquantlibrary PRIVATE
        ${Python3_INCLUDE_DIRS}
        ${Boost_INCLUDE_DIRS}
        ${CMAKE_SOURCE_DIR}/include
        ${CMAKE_SOURCE_DIR}/include/Instrument
        ${CMAKE_SOURCE_DIR}/include/Model
        ${CMAKE_SOURCE_DIR}/include/PricingEngine
        ${CMAKE_SOURCE_DIR}/include/RiskEngine
)
target_link_libraries(pyquantlibrary PRIVATE ${Python3_LIBRARIES} Boost::python model pricing_engine risk_engine)

# Create the main executable
add_executable(quant_library_main src/main.cpp)
target_link_libraries(quant_library_main PRIVATE model pricing_engine risk_engine)

# Set versioning properties for all targets, including the wrapper
set_target_properties(model PROPERTIES VERSION ${PROJECT_VERSION})
set_target_properties(pricing_engine PROPERTIES VERSION ${PROJECT_VERSION})
set_target_properties(risk_engine PROPERTIES VERSION ${PROJECT_VERSION})
set_target_properties(quant_library_main PROPERTIES VERSION ${PROJECT_VERSION})
set_target_properties(pyquantlibrary PROPERTIES VERSION ${PROJECT_VERSION} OUTPUT_NAME "pyquantlibrary" PREFIX "")

# Configure packaging (if needed)
set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
set(CPACK_GENERATOR "TGZ;ZIP")  # Example: you can add other formats like "TGZ", "ZIP", etc.
include(CPack)
