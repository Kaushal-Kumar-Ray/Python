import matplotlib.pyplot as plt
x=[]
y=[]
for i in range(0,5):
    x.append(int(input("Enter no value: ")))
for i in x:
    y.append(i*i*i+i**2-3)         # f(x)=x^3+x^2-3
plt.plot(x,y)
plt.title("User Data")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()