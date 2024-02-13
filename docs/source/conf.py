# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

from pathlib import Path
import sys

if sys.version_info < (3, 11):
    import tomli as tomllib
else:
    import tomllib

from my_package import __version__

# -- Project information -----------------------------------------------------
# see https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information


PROJECT_ROOT_DIR = Path(__file__).parent.parent.parent.resolve()

with open(PROJECT_ROOT_DIR / "pyproject.toml", "rb") as pyproject_toml:
    pyproject_cfg = tomllib.load(pyproject_toml)

project = pyproject_cfg["project"]["name"]
authors = "".join([author["name"] for author in pyproject_cfg["project"]["authors"]])
copyright = f"2023, {authors}"
author = authors
version = __version__
release = version


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.intersphinx",
    "sphinx_copybutton",
    "sphinx.ext.viewcode",
    "breathe",
    "exhale",
    "autoapi.extension",
    "sphinxcontrib.towncrier",
    "sphinx_design",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# Options for towncrier extension
# https://sphinxcontrib-towncrier.readthedocs.io/en/latest/
towncrier_draft_config_path = "towncrier.toml"
towncrier_draft_autoversion_mode = "draft"  # or: 'sphinx-version', 'sphinx-release'
towncrier_draft_include_empty = True
towncrier_draft_working_directory = PROJECT_ROOT_DIR

# Options for sphinx-autoapi
# https://sphinx-autoapi.readthedocs.io/
autoapi_dirs = ["../build/nanobind_stubgen/api/my_package"]
autoapi_root = "api/python/my_package"
autoapi_add_toctree_entry = False
autoapi_keep_files = True
autoapi_template_dir = templates_path[0]

# Options for automodapi extension
# https://sphinx-automodapi.readthedocs.io/en/latest/index.html
numpydoc_show_class_members = False

# Options for Breathe
# https://breathe.readthedocs.io/en/latest/
breathe_projects = {
    "my-package": "../build/xml",
}
breathe_default_project = "my-package"

# Options for Exhale
# https://exhale.readthedocs.io/en/latest/index.html
exhale_args = {
    "containmentFolder": "./api/c++",
    "rootFileName": "library_root.rst",
    "doxygenStripFromPath": "../",
    "rootFileTitle": "C++ Library API",
    # Suggested optional arguments
    "createTreeView": True,
    "contentsDirectives": False,
    # TIP: if using the sphinx-bootstrap-theme, you need
    # "treeViewIsBootstrap": True,
    "exhaleExecutesDoxygen": True,
    "exhaleUseDoxyfile": True,
    # "exhaleDoxygenStdin": "INPUT = ../../include",
}

# Options for intersphinx extension
# https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html
intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "pytest": ("https://pytest.org/en/stable/", None),
    "nanobind": ("https://nanobind.readthedocs.io/en/latest", None),
}


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ["_static"]

html_theme_options = {
    "logo": {"text": "Home"},
    "show_nav_level": 2,
    "navigation_depth": 2,
    "show_toc_level": 2,
    "header_links_before_dropdown": 4,
    "navigation_with_keys": False,
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/HealthyPear/my-package",
            "icon": "fab fa-github-square",
        },
    ],
    "use_edit_page_button": True,
    "announcement": """
        <p>my-package is not stable yet, so expect large and rapid
        changes to structure and functionality before the first stable release</p>
    """,
}

html_context = {
    "github_url": "https://github.com",
    "github_user": "HealthyPear",
    "github_repo": "my-package",
    "github_version": "main",
    "doc_path": "docs",
}
