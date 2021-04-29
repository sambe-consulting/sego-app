# *****************************************************************************#
# Title:                   Middleware init                                     #
# Description:             This is __init__ file contains all the configuration#
#                           needed to run the middleware system                #
# Author:                   Sambe Consulting <development@sambe.co.za>         #
# Original Date:            29 April  2021                                      #
# Version:                  0.1.0                                              #
# *****************************************************************************#


# Importing libraries

from sego.Middleware.MiddlewareManager import MiddlewareManager

# This section we import all middleware to be registered
from .ExampleMiddleware import *

# This section we load middleware using the middlewareManager

middleware_manager = MiddlewareManager()

middleware_manager.load([
    {"name": "example", "middleware": ExampleMiddleware},
    {"name": "example2", "middleware": ExampleMiddleware},
    {"name": "example3", "middleware": ExampleMiddleware},

])

middleware_manager.register(Middleware.PREPROCESS,
                            [
                                'example'
                            ])

middleware_manager.register(Middleware.POSTPROCESS,
                            [
                                'example2'
                            ])
