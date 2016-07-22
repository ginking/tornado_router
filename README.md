
# tornado_router

Decorator based router for Tornado Web Framework that help reduce development time.

[![Build Status](https://travis-ci.org/shicky/tornado_router.svg?branch=master)](https://travis-ci.org/shicky/tornado_router)
[![Coverage Status](https://coveralls.io/repos/github/shicky/tornado_router/badge.svg?branch=master)](https://coveralls.io/github/shicky/tornado_router?branch=master)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/shicky/tornado_router/blob/master/LICENSE)
[![motivation](https://img.shields.io/badge/made%20with-%E2%99%A1-ff69b4.svg)](https://github.com/shicky/tornado_router)

## Why?

Tornado Web Framework requires handler class to be implemented for every request as shown in below example.

```python
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")
```

This is okay for small applications but when you are writing big applications with hundreds of handlers, things quickly get out of hand. Especially since we have to pay extra attention to ensure indentation is correct.

**tornado_router** addresses this issue by providing API to implement decorator-based router. Now, you can type less and pay little attention to indentation. Same example can be reduced to below example.

```python
@router.route()
def index(handler):
    handler.write("Hello, world")
```

It has **no performance disadvantages** compared to class handlers since it constructs handler classes on server startup.

Please click on **Star** if you like this library =)

## Features

**tornado_router** also provides other optional extra features to cut development time.

* Asynchronous authentication and authentication redirect
```python
@router.route(auth=True)
```
* JSON request
```python
@router.route(json=True)
```

* Custom URL Routing (or else URL defaults to method name)
```python
@router.route(url="index")
```

* All Methods supported
```python
@router.route(url="post")
```

# Usage

Below code implements basic authentication

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

* Python 3.4+
* tornado

## Contributing

You are more than welcome to make any contributions.
Please create Pull Request for any changes.

# License

The tornado_router is offered under MIT license.
