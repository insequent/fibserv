#!/usr/bin/python3

from flask import Flask
app = Flask(__name__)

@app.route("/")
def MainHandler():
    """ Single content generating resource that takes a function as input """
    def process_request():
        pass

    return process_request(request.data)

def main(func, port):
    """ This function starts up the flask web server """
    MainHandler.process_request = func
    app.run()
