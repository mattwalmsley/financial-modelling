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

# Add pybind11 submodule
add_subdirectory(extern/pybind11)
if(NOT pybind11_FOUND)
    message(FATAL_ERROR "pybind11 not found")
endif()

# Define the Python wrapper sources
set(PYTHON_WRAPPER_SOURCES
        src/PythonWrapper/PythonWrapper.cpp  # Add your wrapper file here
)


# Define the source files for model, pricing_engine, and risk_engine
set(MODEL_SOURCES
        src/Model/BlackScholesModel.cpp
        src/Model/PricingModel.cpp
        src/Model/Exotics/ADI_Solver.cpp
        src/Model/Exotics/Grid2D.cpp
        src/Model/Exotics/Heston_PDE.cpp
)
set(PRICING_ENGINE_SOURCES
        src/PricingEngine/PricingEngine.cpp  # Replace with your actual pricing engine source files
)
set(RISK_ENGINE_SOURCES
        src/RiskEngine/RiskEngine.cpp  # Replace with your actual risk engine source files
)

# Ensure model, pricing_engine, and risk_engine are built
add_library(model ${MODEL_SOURCES})
target_include_directories(model PUBLIC ${CMAKE_SOURCE_DIR}/include/Model)

add_library(pricing_engine ${PRICING_ENGINE_SOURCES})
target_include_directories(pricing_engine PUBLIC ${CMAKE_SOURCE_DIR}/include/PricingEngine)

add_library(risk_engine ${RISK_ENGINE_SOURCES})
target_include_directories(risk_engine PUBLIC ${CMAKE_SOURCE_DIR}/include/RiskEngine)

add_library(pyquantlibrary MODULE ${PYTHON_WRAPPER_SOURCES})

# Set library output directory for all libraries
set(LIBRARY_OUTPUT_PATH ${CMAKE_BINARY_DIR}/lib)
set_target_properties(model pricing_engine risk_engine PROPERTIES LIBRARY_OUTPUT_DIRECTORY ${LIBRARY_OUTPUT_PATH})

# Include directories for Python, Boost, pybind11, and other relevant headers
target_include_directories(pyquantlibrary PRIVATE
        ${Python3_INCLUDE_DIRS}
        ${pybind11_INCLUDE_DIRS}
        ${CMAKE_SOURCE_DIR}/include
        ${CMAKE_SOURCE_DIR}/include/Instrument
        ${CMAKE_SOURCE_DIR}/include/Model
        ${CMAKE_SOURCE_DIR}/include/PricingEngine
        ${CMAKE_SOURCE_DIR}/include/RiskEngine
)

# Link libraries for Python, pybind11, and any other dependencies
target_link_libraries(pyquantlibrary PRIVATE
        ${Python3_LIBRARIES}
        pybind11::module
        model
        pricing_engine
        risk_engine
)

# Set versioning properties for the target
set_target_properties(pyquantlibrary PROPERTIES
        VERSION ${PROJECT_VERSION}
        OUTPUT_NAME "pyquantlibrary"
        PREFIX ""
        SUFFIX ".so"
)
