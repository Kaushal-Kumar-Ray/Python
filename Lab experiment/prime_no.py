num=int(input("Enter a no:"))
c=0
i=1
while i<=num:
    if num %i==0:
        c=c+1
    i=i+1
if c==2:
    print("Is prime")
else:
    print("not prime")