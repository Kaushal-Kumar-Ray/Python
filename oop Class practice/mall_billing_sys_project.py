class mall:
    def__init__(self,customer,name_pro,total_no_pro,price_per_pro,total):
        self.customer=customer
        self.name=name_pro
        self.total_no_pro=total_no_pro
        self.price_per_pro=price_per_pro
        self.total=total
    def billing(self):
        self.total=self.total_no_pro*self.price_per_pro
    def disp(self):
        print("^^^^^^^^^^^^^^^^^^^      XYZ mall     ^^^^^^^^^^^^^^^^^^^^^^^")
        print("Customer Name:",self.customer)
        print("---------------------------")
        print("-Product Name- \t-Total No of product- \t-Pice per unit \tTotal-")
        print("-----------------------------------------------------------------")
        print(self.name,"\t",self.total_no_pro,"\t\t\t",self.price_per_pro,"\t\t",self.total)        
        print("-----------------------------------------------------------------")
        print("\t\t\tTHANK YOU FOR SHOPING 😃!!!")
        print("******************************************************************")

customer=input("Enter the customer name:") 

name=input("Enter the product name:")
total_no_pro=int(input("Enter the total no of product:"))
price_per_pro=int(input("Enter the price per product:"))
total=0

obj=mall(customer,name,total_no_pro,price_per_pro,total)
obj.billing()
obj.disp()

        