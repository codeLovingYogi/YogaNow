# settings/local.py 
from .settings import *

DEBUG = False
ALLOWED_HOSTS = ['*']
SECRET_KEY=os.environ["MY_SECRET_KEY"]