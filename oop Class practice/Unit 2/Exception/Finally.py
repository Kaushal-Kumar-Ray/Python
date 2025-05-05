"""try:
    x=5/0
except ZeroDivisionError:
    print("zero")
finally:
    print("OK")"""
import os
try:
    x=5/0
except ZeroDivisionError:
    print("zero")
    os._exit(0)
finally:
    print("OK")