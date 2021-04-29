from sego.Middleware.Middleware import Middleware
from sego.Middleware.MiddlewareManager import MiddlewareManager
from webob import Response, Request


class ExampleMiddleware(Middleware):
    def __init__(self):
        pass

    def process_request(self, request: Request):
        print("Processing request", request.url)

    def process_response(self, request: Request, response: Response):
        print("Processing response", Request.url)
