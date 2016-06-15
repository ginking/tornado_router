import uuid
import base64
import tornado_router
import tornado.web
import tornado.httpserver

router = tornado_router.Router(base_handler=tornado_router.BaseHandler)


@router.route(method='get', url='/', auth=True)
def index(handler):
    handler.write('hello tornado!')

@router.route()
def login(handler):
    handler.write('hello login')

def main():

    print(router.requests)

    settings = {
        'cookie_secret': base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes)
    }

    app = tornado.web.Application(router.handlers, **settings)
    app.listen(9000)
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()

