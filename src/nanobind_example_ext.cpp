#include <nanobind/nanobind.h>

namespace nb = nanobind;

using namespace nb::literals;

int add(int a, int b) { return a + b; }

NB_MODULE(nanobind_example_ext, m) {
    m.doc() = "A simple example python extension";
    m.def("add", &add,
          "This function adds two numbers and increments if only one is provided.");
}