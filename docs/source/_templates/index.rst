Python API Reference
====================

The Python3 interface is based on
`nanobind <https://nanobind.readthedocs.io/en/latest/index.html>`_.

Building is performed using
`scikit-build-core <https://scikit-build-core.readthedocs.io/en/latest/index.html>`_.

This page contains auto-generated API reference documentation [#f1]_.

.. toctree::
   :titlesonly:

   {% for page in pages %}
   {% if page.top_level_object and page.display %}
   {{ page.include_path }}
   {% endif %}
   {% endfor %}

.. [#f1] Created with `sphinx-autoapi <https://github.com/readthedocs/sphinx-autoapi>`_