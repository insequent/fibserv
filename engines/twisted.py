"""
Sadly, this engine does not work in Python3, so cannot be used yet.
"""

from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.resource import Resource

class Content(Resource):
    """ Single content generating resource that takes a function as input """
    isLeaf = True

    def __init__(self, func):
        super().__init__()
        self.func = func

    def render_POST(self, request):
        result = self.func(request.content.read())
        return result

def main(func, port):
    """ This function starts up the twisted web server """
    resource = ContentServer(func)
    factory = Site(resource)
    reactor.listenTCP(port, factory)
    reactor.run()
