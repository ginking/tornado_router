
# tornado_router

Decorator based router for Tornado Web Framework that supports asynchronous authentication, json request and more

[![Build Status](https://travis-ci.org/shicky/tornado_router.svg?branch=master)](https://travis-ci.org/shicky/tornado_router)

# Usage

```python
import tornado_router
import tornado.web
import tornado.httpserver

router = tornado_router.Router(base_handler=tornado_router.BaseHandler)

@router.route(method='get', url='/')
def index(handler):
    """ index page """
    handler.write('hello tornado!')

@router.route(method='get', url='/auth_required', auth=True)
def auth_required(handler):
    """ if not authenticated, redirected to login page """
    handler.write('authenticated!')
    
@router.route()
def login(handler):
    """ login page """
    handler.write('login!')
    
def main():
    # print all requests
    print(router.requests)
    app = tornado.web.Application(router.handlers)
    app.listen(9000)
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()
```

# Requirements

* Python_ 3.0+
* tornado_

# License

The tornado_router is offered under MIT license.



[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/shicky/tornado_router/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

