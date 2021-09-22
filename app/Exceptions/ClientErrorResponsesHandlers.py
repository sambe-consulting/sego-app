import sego.Exceptions
from sego.sego import Sego

app = Sego()


def NotFoundHandler(exception):
    views = app.get_view_environment()
    return views.render_view("exceptions/404.html", context={})
app.add_exception_handler(404, NotFoundHandler)
