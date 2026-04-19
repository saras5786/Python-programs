 class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def update_price(self, new_price):
        self.price = new_price

    def buy(self, quantity):
        if quantity <= self.stock:
            self.stock -= quantity
        else:
            print("Insufficient stock")

    def display(self):
        print("Name:", self.name)
        print("Price:", self.price)
        print("Stock:", self.stock)

# main
p = Product("Pen", 10, 5)

print("Before update:")
p.display()
p.update_price(12)
p.buy(2)

print("After update:")
p.display()
