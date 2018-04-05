from .base import *

SECRET_KEY = env('DJANGO_SECRET_KEY', default= '+l$vq9pdw%z3wev))t(w*r%t!w+&r+_a=@_$4%_7+g*7kn)w#i')

DEBUG = env.bool('DJANGO_DEBUG', default=True)