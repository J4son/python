import ctypes
from ctypes import cdll
libc=cdll.LoadLibrary('libc.s0.6')
libc.printf("Hello Wolrd ! ")
