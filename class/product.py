class product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
        print(self.name,self.price)
    def compare(self):
        
n=int(input("Enter the number of items:"))
for i in range(n):
    name=input("Enter the name:")
    price=int(input("Enter the price:"))
objproduct=product(name,price)
