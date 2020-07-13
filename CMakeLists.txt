cmake_minimum_required(VERSION 3.10)

# set the project name
project(mpidb)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

include_directories(src)

# add the executable
add_executable(mpidb src/mpidb.cpp src/Options.cpp)

set_target_properties( mpidb
	PROPERTIES
	RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/bin"
)
