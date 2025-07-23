class HotBeverage:
    price = 0.30
    name = "hot beverage"
    description_str = "Just some hot water in a cup."

    def description(self):
        return self.description_str

    def __str__(self):
        return f"name : {self.name}\nprice : {self.price}\ndescription : {self.description_str}\n"

class Coffee(HotBeverage):
    price = 0.40
    name = "coffee"
    description_str = "A coffee, to stay awake."

class Tea(HotBeverage):
    price = 0.30
    name = "tea"
    description_str = "Just some hot water in a cup."

class Chocolate(HotBeverage):
    price = 0.50
    name = "chocolate"
    description_str = "Chocolate, sweet chocolate..."

class Cappuccino(HotBeverage):
    price = 0.45
    name = "cappuccino"
    description_str = "Un po' di Italia nella sua tazza"
