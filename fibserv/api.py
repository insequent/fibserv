#!/usr/bin/python3

from configparser import ConfigParser
import json
from importlib import import_module

from fibserv.content import Fibonacci


class WebEngineImportError(ImportError):
    pass


class RequestBodyError(TypeError):
    pass


class NegativeCountError(TypeError):
    pass


def main():
    """ This is where everything is initialized """
    # TODO: This should be dynamically loaded from the engines directory.
    #       However, that must wait until twisted works or is removed.
    ENGINES = ["tornado", "flask"]

    cfg = ConfigParser()
    cfg["DEFAULT"] = {"port": "8888",
                      "engine": "flask"}
    cfg["WebServer"] = dict()
    cfg.read("/etc/fibserv/fibserv.conf")

    port = cfg.get("WebServer", "port")
    engine = cfg.get("WebServer", "engine")

    if engine in ENGINES:
        web_engine = import_module("fibserv.engines.{}_engine".format(engine))
    # TODO: Remove this elif once twisted works with Python 3 or is removed
    elif engine == "twisted":
        raise(WebEngineImportError('"twisted" cannot be chosen as a web '
                                   'engine due to it not yet being in Python'
                                   '3. *sad panda*'))
    else:
        raise(WebEngineImportError("Could not import {} as a web engine. "
                                   "Please ensure the file exists in the "
                                   "fibserv/engines/ directory."
                                   "".format(engine)))

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
        raise(RequestBodyError("{} could not be parsed as JSON."
                               "".format(body)))

    if isinstance(body_parsed, int):
        if body_parsed < 0:
            raise(NegativeCountError("'{}' is negative, and alas, Fibonacci "
                                     "sequences can't count backwards from 0."
                                     " Please use a positive number."))
        else:
            result = Fibonacci.sequence(body_parsed)
        return bytes(json.dumps(result), encoding="ASCII")
    else:
        raise(RequestBodyError("{} is not a single number. Please "
                               "try again.".format(body_parsed)))
    return

if __name__ == "__main__":
    main()
