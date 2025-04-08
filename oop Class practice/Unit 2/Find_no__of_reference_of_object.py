import sys
import time
class pk:
    def __init__(self):
        print("Constructor called")
    def __del__(self):
        print("Destructor called")
t=pk()
p=t
x=p
print(sys.getrefcount(t))
p=None
time.sleep(3)
print(sys.getrefcount(t))
time.sleep(3)
print("The end")