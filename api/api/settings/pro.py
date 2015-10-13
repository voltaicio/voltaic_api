from .base import *

ALLOWED_HOSTS = ["api.voltaic.io"]

CORS_ORIGIN_WHITELIST = ("voltaic.io",)

DEBUG = False

MEDIA_ROOT = os.path.join(os.path.sep, "home", "voltaic", "webapps", "media")
MEDIA_URL = "http://api.voltaic.io/media/"

STATIC_ROOT = os.path.join(os.path.sep, "home", "voltaic", "webapps", "static")
STATIC_URL = "http://api.voltaic.io/static/"
