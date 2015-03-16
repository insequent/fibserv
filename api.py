#!/usr/bin/python3

from configparser import ConfigParser
import json
import logging
from importlib import import_module

# TODO: Change this to fibserv.content once packaged
from content import Fibonacci


log = logging.getLogger(__name__)

class WebEngineImportError(ImportError):
    pass

class InvalidBodyData(Exception):
    pass

def main():
    """ This is where everything is initialized """
    # TODO: This should be dynamically loaded from the engines directory
    ENGINES = ["tornado", "flask"]

    cfg = ConfigParser()
    cfg["DEFAULT"] = {"port": "8888",
                      "engine": "flask"}
    # TODO: This would end up in /etc/fibserv once packaged
    cfg.read("fibserv.conf")


    port = cfg.get("WebServer", "port")
    engine = cfg.get("WebServer", "engine")

    if engine in ENGINES:
        # TODO: Change this to "fibserv.engines.{}_engine" once packaged
        web_engine = import_module("engines.{}_engine".format(engine)) 
    else:
        raise(WebEngineImportError("Could not import {} as a web engine. Please "
                                   "ensure the file exists in the "
                                   "fibserv/engines/ directory.".format(engine)))

    web_engine.main(port, process_request)
    return

# NOTE: Need *args here to catch self on class methods
def process_request(*args, body=None):
    """ 
    process_request processes the request body. It takes in the body as a raw
    string and expects it to be JSON, then returns a JSON string as well.
    """
    try:
        body_parsed = json.loads(str(body, encoding="UTF-8"))
    except:
        raise(InvalidBodyData("'{}' couldn't be parsed as JSON.".format(body)))

    if isinstance(body_parsed, int):
        return bytes(json.dumps(Fibonacci.sequence(body_parsed)),
                     encoding="ASCII")
    else:
        raise(InvalidBodyData("'{}' is not a single number. Please "
                              "try again.".format(body_parsed)))
    return

if __name__ == "__main__":
    main()
