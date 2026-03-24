class Product():
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __str__(self):
        return (self.name)

    def get_information(self):
        information = "Product: " + self.name + " | Price: " + self.price
        return information

class Client():
    def __init__(self, name, email, shopping_cart):
        self.name = name
        self.email = email
        self.shopping_cart = []
    def __str__(self):
        return (self.name)

    def add_to_cart(self, product):
        self.shopping_cart.append(product)

    def compute_total(self):
        total = 0
        for i in self.shopping_cart:
            total += i.price
        return total

class VIPClient(Client):
    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.discount = discount
    def __str__(self):
        return (self.name)

    def compute_total(self):
        total = super().compute_total()
        percent_discount = 1 - (self.discount / 100)
        return total * percent_discount