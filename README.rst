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
For example, to install the "0.1.0" tag (or release) do

```bash

  pip install git+https://github.com/desihub/desibgs.git@0.1.0
  
```  

Alternatively, you can clone the master branch from `Github`_ 
  
```bash

  git clone git@github.com:desihub/desibgs.git
  
```  

and then either install the package to an installation directory of your
choice

```python

  python setup.py install --prefix=$INSTALL_DIR
  
```

or explicitly add the code directory to you $PYTHONPATH, e.g.

```bash

  export PYTHONPATH=/path/to/desibgs/py:$PYTHONPATH
  
  export PATH=/path/to/desibgs/bin:${PATH}
  
```

.. _pip: http://pip.readthedocs.org
.. _Github: http://https://github.com

Product Contents
================

bin/
    Executable scripts.
doc/
    High-level documentation (.rst files).
etc/
    Small data and configuration files.
py/
    Python code.

License
=======

desibgs is free software licensed under a 3-clause BSD-style license. For details see
the ``LICENSE.rst`` file.
