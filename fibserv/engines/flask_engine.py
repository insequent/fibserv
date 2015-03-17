#!/usr/bin/python3

import logging

from flask import Flask
from flask import request
from flask import Response


app = Flask(__name__)
log = logging.getLogger(__name__)


# NOTE: A class isn't required here per se, but including one to stay
#       semi-consitent with other engines.

class MainHandler(object):
    """ Single content generating resource that takes a function as input """
    @classmethod
    def apply_content(cls, func):
        cls.process_request = func

    @staticmethod
    def process_request():
        pass


@app.route("/", methods=["POST"])
def post():
    data = request.get_data()
    result = MainHandler.process_request(body=data)
    return Response(result, mimetype='application/json')


def main(port, func):
    """ This function starts up the flask web server """
    MainHandler.apply_content(func)
    app.run(port=int(port))  # NOTE: Flask requires an int here


if __name__ == "__main__":
    main(8888, lambda *args, **kwargs: "IT WORKS!")
