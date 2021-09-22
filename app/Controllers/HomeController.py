# ************************************************************************#
# Title:                    Home Controller                               #
# Description:              This class houses all actions related to      #
#                           the homepage                                  #
# Author:                   Sambe Consulting <development@sambe.co.za>    #
# Original Date:            23 March 2021                                 #
# Version:                  0.1.0                                         #
# ************************************************************************#

from . import BaseController


class HomeController(BaseController):

    def index(self):
        return self.Views.render_view("home.html")
