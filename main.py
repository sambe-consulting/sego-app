from sego.sego import Sego
from sego.Views.Views import Views
sego_app = Sego(application_name="application")


exception_packages = "app.Exceptions"
routes_package_path = "app.routes"
middleware_package_path = "app.Middleware"
credentials = {"config_path":"app/Configurations/"}
templates_dir = "app/templates"
static_files_dir = "app/public"

views = Views(view_path=templates_dir)
sego_app.register_middleware(middleware_package_path)
sego_app.register_exception_handlers(exception_packages)
sego_app.register_static_files(static_dir=static_files_dir)
sego_app.register_views(views)
sego_app.register_configurations(credentials=credentials,)
sego_app.register_routes(routes_package_path)
sego_app.register_database()
sego_app.setup_app()
# For dev use only.
sego_app.dev_run(port=9001)

# For production use with WSGI server
#
app = sego_app.get_app()
#

