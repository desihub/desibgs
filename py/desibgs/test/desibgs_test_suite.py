# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-
"""
desibgs.test.desibgs_test_suite
===============================

Used to initialize the unit test framework via ``python setup.py test``.
"""
#
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
#
import unittest

def desibgs_test_suite():
    """Returns unittest.TestSuite of desibgs tests.

    This is factored out separately from runtests() so that it can be used by
    ``python setup.py test``.
    """
    from os.path import dirname
    py_dir = dirname(dirname(__file__))
    # print(py_dir)
    return unittest.defaultTestLoader.discover(py_dir,
                                               top_level_dir=dirname(py_dir))


def runtests():
    """Run all tests in desibgs.test.test_*.
    """
    # Load all TestCase classes from desibgs/test/test_*.py
    tests = desibgs_test_suite()
    # Run them
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == "__main__":
    runtests()
