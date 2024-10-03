cmake_minimum_required(VERSION 3.10)

# Set the project name
project(SpotHintaApp)

# Find the required packages
find_package(Crow CONFIG REQUIRED)
find_package(CPR CONFIG REQUIRED)
find_package(nlohmann_json CONFIG REQUIRED)

# Create an executable
add_executable(spot-hinta app.cpp)

# Link the libraries
target_link_libraries(spot-hinta PRIVATE Crow::crow CPR::cpr nlohmann_json::nlohmann_json)