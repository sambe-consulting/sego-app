import sego.Exceptions
from sego.sego import Sego

app = Sego()


def NotFoundHandler(request, response, exception):
    views = app.get_view_environment()
    response.text = views.render_view("tests/index.html", context={"name": "name", "title": "framework"})


app.add_exception_handler(sego.Exceptions.NotFoundException404, NotFoundHandler)
