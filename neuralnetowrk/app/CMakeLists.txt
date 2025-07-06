cmake_minimum_required(VERSION 3.5.1)

project(house-price-prediction-fhe CXX)
set(CMAKE_CXX_STANDARD 17)
option(BUILD_STATIC "Set to ON to include static versions of the library" OFF)

# Point to your local OpenFHE installation
set(CMAKE_PREFIX_PATH "${CMAKE_CURRENT_SOURCE_DIR}/../openfhefiles")
set(CMAKE_PREFIX_PATH "/mingw64" ${CMAKE_PREFIX_PATH})

find_package(OpenFHE REQUIRED)

set(CMAKE_CXX_FLAGS ${OpenFHE_CXX_FLAGS})

include_directories(${OPENMP_INCLUDES})
include_directories(${OpenFHE_INCLUDE})
include_directories(${OpenFHE_INCLUDE}/third-party/include)
include_directories(${OpenFHE_INCLUDE}/core)
include_directories(${OpenFHE_INCLUDE}/pke)
include_directories(${OpenFHE_INCLUDE}/binfhe)
include_directories(${OpenFHE_INCLUDE}/core/utils)
include_directories(${OpenFHE_INCLUDE}/cereal/archives)
include_directories(${OpenFHE_INCLUDE}/cereal/types)
include_directories(${OpenFHE_INCLUDE}/pke/keys)
include_directories(${CMAKE_CURRENT_SOURCE_DIR})  # Include current directory for json.hpp

link_directories(${OpenFHE_LIBDIR})
link_directories(${OPENMP_LIBRARIES})

# Add executables
add_executable(app 
    main.cpp 
    yourSolution.cpp  # Add the implementation file here
)

# Linking libraries based on BUILD_STATIC option
if (BUILD_STATIC)
    set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -static")
    target_link_libraries(app ${OpenFHE_STATIC_LIBRARIES})
else()
    target_link_libraries(app ${OpenFHE_SHARED_LIBRARIES})
endif()

# Print message to confirm paths
message(STATUS "OpenFHE include dirs: ${OpenFHE_INCLUDE}")
message(STATUS "OpenFHE libraries: ${OpenFHE_SHARED_LIBRARIES}")
message(STATUS "OpenFHE libdir: ${OpenFHE_LIBDIR}")