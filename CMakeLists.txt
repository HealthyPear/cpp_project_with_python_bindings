cmake_minimum_required(VERSION 3.27)

project(
    ${SKBUILD_PROJECT_NAME}
    VERSION ${SKBUILD_PROJECT_VERSION}
    DESCRIPTION "My awesome package"
    LANGUAGES CXX
)

# provides CMAKE_INSTALL_BINDIR / CMAKE_INSTALL_LIBDIR etc. with sane defaults
include(GNUInstallDirs)

# set a default value for the build type
# (Debug if inside a git repository, Release otherwise)
# and also validate the given type
include(cmake/BuildType.cmake)

# add proper RPATH to build and install libraries and executables
# so that setting an ``LD_LIBRARY_PATH`` is unnecessary
include(cmake/RPATHHandling.cmake)

find_package(Python 3.9 COMPONENTS Interpreter Development.Module REQUIRED)

# Detect the installed nanobind package and import it into CMake
execute_process(
    COMMAND " ${Python_EXECUTABLE} " -m nanobind --cmake_dir
    OUTPUT_STRIP_TRAILING_WHITESPACE OUTPUT_VARIABLE NB_DIR)
list(APPEND CMAKE_PREFIX_PATH " ${NB_DIR} ")
find_package(nanobind CONFIG REQUIRED)

nanobind_add_module(nanobind_example_ext src/nanobind_example_ext.cpp)

install(TARGETS nanobind_example_ext LIBRARY DESTINATION ${SKBUILD_PROJECT_NAME})