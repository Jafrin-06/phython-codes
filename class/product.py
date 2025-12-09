class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def compare(self):
        if self.price > price:
            return 
        elif self.price < price:
            return 
        else:
            return 


name1 = input("Enter Product 1 name: ")
price1 = float(input("Enter Product 1 price: "))
name2 = input("Enter Product 2 name: ")
price2 = float(input("Enter Product 2 price: "))
p1 = Product(name1, price1)
p2 = Product(name2, price2)
print(p1.compare(p2))
