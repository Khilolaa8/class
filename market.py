# classes =  product, company, basket

# Product
# attribute - name, price, quantity, company
# methods - print()

# Company
# attribute - name, yil
# methods - info()

# Basket
# attribute - products
# methods - add_product(), remove_product(), view(), total_price()

class Product:
    def __init__(self, name, price, quantity, company):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.company = company


    def __str__(self):
        print(f"Product Name: {self.name}, Price: {self.price}, Quantity: {self.quantity},Company: {self.company}")


class Company:
    def __init__(self,name,yil):
        self.name = name
        self.yil = yil

    def __str__(self):
        print(f"Company name: {self.name}, Year: {self.yil}")


class Basket:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        for item in self.products:
            if item.name ==  product.name:
                item.quantity += product.quantity
                return
        self.products.append(product)
        # print(f"Added {product.name} to the basket.")

    def view_products(self):
        for product in self.products:
            print(product)





