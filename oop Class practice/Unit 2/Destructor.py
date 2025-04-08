import time 
class pk:
    def __init__(self):
        print("Constructor called")
    def __del__(self):
        print("Destructor called")
pk=pk()
p=None
print(pk)
print("Garbage collecctor is deleting object")
time.sleep(3)
print("End of program")