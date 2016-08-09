# settings/local.py 
from .settings import *

DEBUG = True
ALLOWED_HOSTS = [*]
SECRET_KEY=os.environ["MY_SECRET_KEY"]