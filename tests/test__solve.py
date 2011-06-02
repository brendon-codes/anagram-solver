#!/usr/bin/env python

import unittest

from anagram import solve


class TestSolve(unittest.TestCase):

    def test_runner_1(self):
        data = "Herlo wolld"
        out, score = solve.runner(data)
        self.assertTrue(score > 0)
        return True


if __name__ == '__main__':
    unittest.main()
