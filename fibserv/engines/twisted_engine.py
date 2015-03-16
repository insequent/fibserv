"""
Sadly, by switching to python 3, this engine can no longer be used.
Twisted needs to catch up with the times.
"""

from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.resource import Resource


class MainHandler(Resource):
    """ Single content generating resource that takes a function as input """
    isLeaf = True

    def __init__(self, func):
        super().__init__()
        self.func = func

    def render_POST(self, request):
        result = self.func(body=request.content.read())
        return result


def main(port, func):
    """ This function starts up the twisted web server """
    resource = MainHandler(func)
    factory = Site(resource)
    reactor.listenTCP(port, factory)
    reactor.run()
