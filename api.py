#!/usr/bin/python3

from configparser import ConfigParser
from importlib import import_module
from os import path


class WebEngineImportError(ImportError):
    pass


def main():
    """ This is where everything is initialized """
    #NOTE: Although a "twisted" engine is coded, it cannot be used in Python 3
    ENGINES = ["tornado", "flask"]

    cfg = ConfigParser()
    cfg["DEFAULT"] = {"port": "8888",
                      "engine": "tornado"}
    cfg.read("fibserv.conf")


    PORT = cfg.get("WebServer", "port")
    engine = cfg.get("WebServer", "engine")

    if engine in ENGINES:
        ENGINE = import_module("engines.{}".format(engine)) 
    else:
        raise(WebEngineImportError("Could not import {} as a web engine. Please "
                                   "ensure the file exists in the "
                                   "fibserv/engines/ directory.".format(engine)))

    print(ENGINE, PORT)

if __name__ == "__main__":
    main()
