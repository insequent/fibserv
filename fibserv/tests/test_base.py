#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest


class TestBase(unittest.TestCase):
    """Base all test classes in fibserv."""

    def setUp(self):
        super(TestBase, self).setUp()
