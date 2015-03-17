#!/usr/bin/python3

import unittest.mock as mock

from fibserv import api
from fibserv.tests import test_base


class FibServAPITest(test_base.TestBase):
    @mock.patch('fibserv.api.ConfigParser.get')
    def test_api_main(self, mock_config):
        """ Testing the main function in fibserv/api.py """
        mock_config.side_effect = ('80', 'not_real')

        self.assertRaises(ImportError, api.main)

    @mock.patch('fibserv.api.Fibonacci.sequence')
    def test_api_process_request(self, mock_seq):
        """ Testing the process_request function in fibserv/api.py """
        mock_seq.return_value = "WORKS"

        self.assertEqual(api.process_request(body=b'1'), b'"WORKS"')
        self.assertTrue(mock_seq.called_with(1))
        self.assertRaisesRegexp(Exception,
                                r".*could\ not\ be\ parsed\ as\ JSON\.$",
                                api.process_request,
                                body=object())
        self.assertRaisesRegexp(Exception,
                                r".*is\ not\ a\ single\ number\..*$",
                                api.process_request,
                                body=b'"string"')
