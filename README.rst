=======
desibgs
=======

.. image:: https://img.shields.io/travis/desihub/desibgs.svg
    :target: https://travis-ci.org/desihub/desibgs
    :alt: Travis Build Status
.. image:: https://coveralls.io/repos/desihub/desibgs/badge.svg?service=github
    :target: https://coveralls.io/github/desihub/desibgs
    :alt: Test Coverage Status
.. image:: https://readthedocs.org/projects/desibgs/badge/?version=latest
    :target: http://desibgs.readthedocs.org/en/latest/
    :alt: Documentation Status

Introduction
============

This repository contains code and documentation for the DESI_ Bright Galaxy
Survey (BGS).  For full documentation please visit `desibgs on Read the Docs`_.

.. _DESI: https://desi.lbl.gov
.. _`desibgs on Read the Docs`: http://desibgs.readthedocs.org/en/latest/

Installation
============

This product is installable using pip_ or it can cloned directly from `Github`_.
For example, to install the "0.1.0" tag (or release) do::

  pip install git+https://github.com/desihub/desibgs.git@0.1.0

Alternatively, to clone the master branch from `Github`_ do::
  
  git clone git@github.com:desihub/desibgs.git

Then you can either install the package to an appropriate directory

  python setup.py install --prefix=$INSTALL_DIR

or explicitly add the code directory to you $PYTHONPATH, e.g.

  export PYTHONPATH=/path/to/desibgs/py:$PYTHONPATH
  export PATH=/path/to/desibgs/bin:${PATH}
  
.. _pip: http://pip.readthedocs.org
.. _Github: http://https://github.com

Product Contents
================

Directory Structure
~~~~~~~~~~~~~~~~~~~

bin/
    Executable scripts.
doc/
    High-level documentation (.rst files), which will be processed by Sphinx_.
etc/
    Small data and configuration files.
py/
    Python code.

.. _Sphinx: http://sphinx-doc.org

Additional Support Files
~~~~~~~~~~~~~~~~~~~~~~~~

In addition to the standard ``.gitignore`` file, there are two other
hidden files included in this product.

.coveragerc
    Configuration for the test coverage.

.travis.yml
    Configuration file for `Travis CI`_ tests.

requirements.txt
    The requirements.txt file contains other Python packages required by this
    package which will be processed during Travis tests to install packages
    needed for the tests.  This file is processed with the command::

        pip install -r requirements.txt

MANIFEST.in
    This file contains instructions for the setup system that will be used to
    construct an "official" tarball of the package.  For example, this file will
    be used by the command::

        python setup.py sdist

    This file is absolutely necessary if your package will be distributed via
    PyPI_.

.module
    In the etc/ directory is a file called ``desibgs.module``.  This file is
    used to create a module file for the product at install time.  This file is
    intended for use at NERSC_; it is not processed automatically by pip.

_version.py
    This file is created and maintained by the command::

        python setup.py version

.. _PyPI: http://pypi.python.org
.. _`Travis CI`: http://travis-ci.org

License
=======

desibgs is free software licensed under a 3-clause BSD-style license. For details see
the ``LICENSE.rst`` file.
