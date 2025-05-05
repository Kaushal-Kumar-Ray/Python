class pqr:
     def __init__(self):
         print("Constructor executed")
     def __del__(self):
         print("Destructor executed")
p=pqr()
t=p
del(t)
del(p)
        