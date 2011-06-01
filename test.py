#!/usr/bin/python

"""
Test runner
Not using nose, since this needs to reliably run on machines
that might not have nose installed.
"""

import os
import sys
import unittest

dname = os.path.dirname(__file__)
rname = os.path.realpath(dname + '/../')
sys.path.append(rname)
os.chdir(dname)


if __name__ == '__main__':
    unittest.main(module='tests.test__solve')
