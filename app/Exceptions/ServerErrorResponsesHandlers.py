from sego.sego import Sego
from sego.Exceptions.ConfigurationException import ConfigurationNotLoadedException
import confo.Exceptions

sego = Sego()


def ConfigHandler(request, response, exception):
    views = sego.get_view_environment()
    response.text = views.render_view("tests/index.html", context={"name": "name", "title": "framework"})


# sego.add_exception_handler(confo.Exceptions.BackendsActivationException, ConfigHandler)

