import sego.Exceptions
from sego.sego import Sego

app = Sego()


def NotFoundHandler(request, response, exception):
    views = app.get_view_environment()
    response.status_code = 404
    response.text = views.render_view("exceptions/404.html", context={})


app.add_exception_handler(sego.Exceptions.NotFoundException404, NotFoundHandler)
