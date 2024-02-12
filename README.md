# my-package

![ci](https://github.com/github/docs/actions/workflows/ci.yml/badge.svg?branch=main)
![deploy](https://github.com/github/docs/actions/workflows/deploy.yml/badge.svg?branch=main)

This project template is designed for C++ projects providing Python3 bindings.

This project is built from C++ using
`scikit-build-core <https://scikit-build-core.readthedocs.io/en/latest/index.html>`_
to make a bridge between [CMake](https://cmake.org/) and the Python build system and make Python modules with CMake.

The Python bindings are built with `nanobind <https://nanobind.readthedocs.io/en/latest/index.html>`_.

# Installation

Since there is no release yet, the only installation
available is the development version.

> [!TIP]
> The use of a virtual environment is recommended;
  a [conda](https://docs.conda.io/projects/conda/en/stable/user-guide/index.html) environment
  file is provided (if you start from scratch is recommended to
  install the [Miniforge3](https://github.com/conda-forge/miniforge) distribution which comes with [mamba](https://mamba.readthedocs.io/) as a faster alternative to `conda`).
  In the following instructions this is the assumed setup.

1. [create a new repository from this template](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template)
2. [clone your newly created repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
2. `cd your_repo_name`
3. search and replace globally `my-package` and `my_package` with the equivalent of your project name identifiers
2. `conda env create -f environment.yml` (`mamba` is recommended over `conda` if available)
3. `pip install .[dev]`
4. `pre-commit install`

# Update

1. Switch to the default branch and update it (`git switch main && git pull`)
2. activate the development virtual environment (`conda activate your-env-name`)
3. update it (`conda env update --file environment.yml --prune`)
4. re-install the package (`pip install .[dev]`)

# Documentation

The documentation is based on [](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)
and build using,

- [pydata-sphinx-theme]() as the theme,
- [rstcheck](https://rstcheck.readthedocs.io/en/latest/) as a linter
- [towncrier](https://towncrier.readthedocs.io/)
   and [sphinxcontrib-towncrier](https://sphinxcontrib-towncrier.readthedocs.io/en/latest/)
   for the build of the changelog,
- [nanobind-stubgen](https://github.com/cansik/nanobind-stubgen) and [sphinx-autoapi](https://sphinx-autoapi.readthedocs.io/)
   to generate the Python bindings API documentation automatically
- [Doxygen](https://www.doxygen.nl/), [breathe](https://breathe.readthedocs.io/)
  and [exhale](https://exhale.readthedocs.io/en/latest/index.html)
  to generate automatically the C++ API

Documentation can be compiled locally with `make -C docs html` (a `clean` target is also available).

# Development

The development process is based on a
[pre-commit](https://pre-commit.com/) configuration.

Linting and formatting are performed using
[ruff](https://docs.astral.sh/ruff/).

Testing for the Python interface is performed with [pytest](https://docs.pytest.org/en/latest/)
while that for the C++ interface needs to be added.