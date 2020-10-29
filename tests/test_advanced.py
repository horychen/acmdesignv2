# -*- coding: utf-8 -*-

from .context import _tuner, _simulator, _analyzer

import unittest

class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(sample.hmm())


if __name__ == '__main__':
    unittest.main()
