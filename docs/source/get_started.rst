.. _getstarted:

===========
Get started
===========

.. _conda: https://docs.conda.io/projects/conda/en/stable/user-guide/index.html
.. _miniforge: https://github.com/conda-forge/miniforge
.. _mamba: https://mamba.readthedocs.io/


Installation
============

Since there is no release yet, the only installation
available is the **development** version.

Users
-----

This type of installation will be available as soon as a release is deployed.

.. tab-set::

    .. tab-item:: pip

        .. code-block:: shell

          pip install my-package

    .. tab-item:: conda

        .. code-block:: shell

          conda install my-package

Developers
----------

.. tip::
  
  The use of a virtual environment is recommended;
  a `conda`_ environment
  file is provided (if you start from scratch is recommended to
  install the `miniforge`_ distribution which comes with `mamba`_ as a faster alternative to ``conda``).
  In the following instructions this is the assumed setup.

1. `create a new repository from this template <https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template>`_
2. `clone your newly created repository <https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository>`_
3. ``cd cloned_repo_name``
4. ``conda env create -f environment.yml`` (``mamba`` is recommended over ``conda`` if available)
5. ``pip install .[dev]``
6. ``pre-commit install``

# Update

1. Switch to the default branch and update it (``git switch main && git pull``)
2. activate the development virtual environment (``conda activate your-env-name``)
3. update it (``conda env update --file environment.yml --prune``)
4. re-install the package (``pip install .[dev]``)
5. update the pre-commit hooks (``precommit install``)