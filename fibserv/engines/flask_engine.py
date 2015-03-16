#!/usr/bin/python3

import logging

from flask import Flask
from flask import request
from flask import Response

app = Flask(__name__)
log = logging.getLogger(__name__)


def main(port, func):
    """ This function starts up the flask web server """

    @app.route("/", methods=["POST"])
    def MainHandler():
        """ Main content generating resource """
        data = request.get_data()
        try:
            result = func(body=data)
        except:
            log.exception("func failed to execute with "
                          "'{}'".format(data))
        return Response(result, mimetype='application/json')

    app.run(port=int(port))  # Flask requires int here
