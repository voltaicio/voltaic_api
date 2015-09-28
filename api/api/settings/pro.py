from .base import *

ALLOWED_HOSTS = ["api.voltaic.io"]

CORS_ORIGIN_WHITELIST = ("voltaic.io",)

DEBUG = False

STATIC_ROOT = os.path.join(os.path.sep, "home", "voltaic", "webapps", "static")
STATIC_URL = "http://api.voltaic.io/static/"
