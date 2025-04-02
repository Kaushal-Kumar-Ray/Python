no=int(input("Enter a 1 to start:"))
while 1:
    print("Press 1 to calculate Factorial")
    print("Press 2 to check Prime")
    print("Press 3 to check Armstrong")
    print("Press 4 to EXIT")
    print("-----------------------------------------")
    choice=int(input("Enter your choice"))
    
    if choice==1:
        num=int(input("Enter a no:"))
        fact =1
        for i in range(1,num+1):
           fact=fact*i
        print(f"----Factorial of {num} is {fact}----")   
    
    elif choice==2:
        num=int(input("Enter a no:"))
        c=0
        i=1
        while i<=num:
            if num %i==0:
                c=c+1
            i=i+1
        if c==2:
             print("----Is prime----")
        else:
            print("----Not prime----") 
    
    elif choice==3:
        s=0
        n=int(input("Enter no:"))
        y=n
        c=len(str(n))
        while n>0:
            r=n%10
            n=n//10
            s=s+r**c
        if s==y:
            print(f"----{s} Is a Armstrong----")
        else:
            print("----Not an Armstrong----")
    elif choice==4:
        print("----GOOD BYE\U0001F600----") 
        break
    else:
        print("----Invalid choice\U0001F695----")


