try:
    x=int(input("Enter a number: "))
    y=int(input("Enter a number: "))
    z=x/y
except ZeroDivisionError:
    z=x/2
    print("Humm",z)
except TypeError:
    print("Invalid Input")
print("Checked")