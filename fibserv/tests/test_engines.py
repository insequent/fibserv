#!/usr/bin/python3

import unittest.mock as mock

from fibserv.engines import flask_engine
from fibserv.engines import tornado_engine
from fibserv.tests import test_base


class FibServEnginesTest(test_base.TestBase):
    @mock.patch('fibserv.engines.flask_engine.Response')
    @mock.patch('fibserv.engines.flask_engine.request')
    @mock.patch('fibserv.engines.flask_engine.Flask.route')
    @mock.patch('fibserv.engines.flask_engine.Flask.run')
    def test_flask_engine(self, mock_run, mock_route,
                          mock_request, mock_response):
        """ For testing fibserv/engines/flask_engine.py """
        class mock_deco(object):
            # NOTE: This throws away all arguments passed to the decorator.
            def __init__(self, *args, **kwargs):
                pass

            # NOTE: This throws away all arguments passed to the decorated
            #       function and executes it.
            def __call__(self, fn):
                def wrapped(*args, **kwargs):
                    return fn()
                return wrapped
 
        mock_route.side_effect = mock_deco
        mock_response.return_value = "MY RESPONSE"

        flask_engine.main(443, lambda **kwargs: "PASS")
        flask_engine.post()

        mock_run.assert_called_with(port=443)
        self.assertTrue(mock_response.called)
        mock_response.assert_called_with('PASS', mimetype='application/json')

    @mock.patch('fibserv.engines.tornado_engine.tornado.ioloop.IOLoop.instance')
    @mock.patch('fibserv.engines.tornado_engine.tornado.log.enable_pretty_logging')
    @mock.patch('fibserv.engines.tornado_engine.tornado.web.Application.listen')
    def test_tornado_engine(self, mock_listen, mock_log, mock_instance):
        """ For testing fibserv/engines/tornado_engine.py """
        tornado_engine.main(443, lambda **kwargs: "PASS")

        mock_listen.assert_called_with(443)
        self.assertTrue(mock_log.called)
        self.assertTrue(mock_instance.called)
