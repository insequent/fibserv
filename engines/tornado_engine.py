import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    """ Single content generating resource that takes a function as input """
    @classmethod
    def content_function(cls, func):
        cls.process_request = func

    @staticmethod
    def process_request():
        pass

    def post(self):
        result = self.process_request(body=self.request.body)
        self.write(result)

def main(port, func):
    """ This function starts up the tornado web server """
    MainHandler.content_function(func)
    application = tornado.web.Application([(r"/", MainHandler)])
    application.listen(port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
