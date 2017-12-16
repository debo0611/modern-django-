from .base import *

SECRET_KEY = env('DJANGO_SECRET_KEY',
                 default='p#xq!7%$e!f_z$^1$no0n4n4%c+p_)@#sx4&u4!ncy%gvwb)_r')

DEBUG = env.bool('DJANGO_DEBUG', default=True)
