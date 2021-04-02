

from sego.sego import Sego
from sego.Views.Views import Views
app = Sego()


views = Views(view_path="app/templates/")
exception_packages = "app.Exceptions"
routes_package_path = "app.routes"
credentials = {"config_path":"app/Configurations/"}

app.register_exception_handlers(exception_packages)
app.register_views(views)
app.register_configurations(credentials=credentials,)
app.register_routes(routes_package_path)

