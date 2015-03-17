#!/usr/bin/python3

import unittest.mock as mock

from fibserv.content import Fibonacci as fib
from fibserv.tests import test_base


class FibServContentTest(test_base.TestBase):
    def test_Fibonacci(self):
        """ Tests fibserv/content/Fibonacci.py """
        self.assertEqual(fib.sequence(0), tuple())
        self.assertEqual(fib.sequence(1), (0,))
        self.assertEqual(fib.sequence(2), (0,1))
        self.assertEqual(fib.sequence(3), (0,1,1))
        self.assertEqual(fib.sequence(4), (0,1,1,2))
        self.assertRaises(TypeError, fib.sequence, 'puppies')
