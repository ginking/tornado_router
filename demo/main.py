import tornado_router
import tornado.web
import tornado.httpserver

router = tornado_router.Router(base_handler=tornado_router.BaseHandler)


@router.route(method='post', url='/')
def index(handler):
    print('hello')
    handler.write('hello')


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('hello')

def main():

    print(router.handlers[0][1])
    #print(router.requests)

    handlers = [(r"/", MainHandler)]
    app = tornado.web.Application(handlers)
    app.listen(9000)
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()

