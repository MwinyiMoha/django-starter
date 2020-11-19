import os


if "DEPL_ENV" in os.environ:
    if os.environ["DEPL_ENV"] == "PRODUCTION":
        from .production import *
    else:
        from .staging import *
else:
    from .local_settings import *
