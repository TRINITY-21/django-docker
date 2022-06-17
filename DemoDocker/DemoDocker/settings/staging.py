from .base import *

# DEBUG = False

DEBUG = int(os.environ.get("DEBUG", default=2))


try:
    from .local import *
except ImportError:
    pass
