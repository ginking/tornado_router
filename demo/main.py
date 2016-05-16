import tornado_router
import tornado.web
import tornado.httpserver

router = tornado_router.Router(base_handler=tornado_router.BaseHandler)


@router.route(method='get', url='/')
def index(handler):
    handler.write('hello tornado!')


def main():

    print(router.requests)

    app = tornado.web.Application(router.handlers)
    app.listen(9000)
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()

