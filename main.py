

from sego.sego import Sego
from sego.Views.Views import Views
app = Sego()


exception_packages = "app.Exceptions"
routes_package_path = "app.routes"
middleware_package_path = "app.Middleware"
credentials = {"config_path":"app/Configurations/"}
templates_dir = "app/templates"
static_files_dir = "app/public"

views = Views(view_path=templates_dir)
app.register_middleware(middleware_package_path)
app.register_exception_handlers(exception_packages)
app.register_static_files(static_dir=static_files_dir)
app.register_views(views)
app.register_configurations(credentials=credentials,)
app.register_routes(routes_package_path)

