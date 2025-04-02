s=0
n=int(input("Enter no:"))
y=n
c=len(str(n))
while n>0:
    r=n%10
    n=n//10
    s=s+r**c
if s==y:
   print(f"{s} is a Armstrong")
else:
    print("The number is not an armstrong")