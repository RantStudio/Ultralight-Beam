class item:
    def __init__(self, name, price, color, buylink, category):
        self.name = name
        self.price = price
        self.color = color
        self.buylink = buylink
        self.category = category


class category:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
