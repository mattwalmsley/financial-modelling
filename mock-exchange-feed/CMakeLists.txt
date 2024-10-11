cmake_minimum_required(VERSION 3.10)
project(MockExchangeFeed)

set(CMAKE_CXX_STANDARD 17)

# Include directories
include_directories(include)

# Find and include ZeroMQ
find_package(PkgConfig REQUIRED)
pkg_check_modules(ZeroMQ REQUIRED libzmq)

# Find and include Boost
find_package(Boost REQUIRED)

# Source files
set(SOURCES
        src/main.cpp
        src/feed_generator.cpp
)

# Executable
add_executable(mock_feed ${SOURCES})

# Link libraries
target_link_libraries(mock_feed ${Boost_LIBRARIES} ${ZeroMQ_LIBRARIES})
