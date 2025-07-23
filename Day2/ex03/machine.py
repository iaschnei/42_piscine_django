from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino
import random

class CoffeeMachine:
    def __init__(self):
        self.num_of_use_left = 10
        random.seed(10)
    
    class EmptyCup(HotBeverage):
        price = 0.90
        name = "empty cup"
        description_str = "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__("This coffee machine has to be repaired")

    def repair(self):
        self.num_of_use_left = 10

    def serve(self, beverage : HotBeverage):
        if not isinstance(beverage, HotBeverage):
            raise TypeError("Expected an hotbeverage")
        if self.num_of_use_left == 0:
            raise self.BrokenMachineException()
        self.num_of_use_left -= 1
        result = random.randint(0, 1)
        if result == 1:
            return self.EmptyCup()
        else:
            return beverage
    


def main():
    coffeeMachine = CoffeeMachine()
    beverage = coffeeMachine.serve(Coffee())
    print(beverage)
    beverage = coffeeMachine.serve(Tea())
    print(beverage)
    beverage = coffeeMachine.serve(Chocolate())
    print(beverage)
    beverage = coffeeMachine.serve(Tea())
    print(beverage)
    beverage = coffeeMachine.serve(Tea())
    print(beverage)
    beverage = coffeeMachine.serve(Tea())
    print(beverage)
    beverage = coffeeMachine.serve(Tea())
    print(beverage)
    beverage = coffeeMachine.serve(Tea())
    print(beverage)
    beverage = coffeeMachine.serve(Tea())
    print(beverage)
    beverage = coffeeMachine.serve(Tea())
    print(beverage)
    try:
        beverage = coffeeMachine.serve(Tea())
        print(beverage)
    except Exception as e:
        print(e)
    coffeeMachine.repair()
    beverage = coffeeMachine.serve(Tea())
    print(beverage)
    beverage = coffeeMachine.serve(Tea())
    print(beverage)
    beverage = coffeeMachine.serve(Tea())
    print(beverage)
    beverage = coffeeMachine.serve(Tea())
    print(beverage)
    beverage = coffeeMachine.serve(Tea())
    print(beverage)
    beverage = coffeeMachine.serve(Tea())
    print(beverage)
    beverage = coffeeMachine.serve(Tea())
    print(beverage)
    beverage = coffeeMachine.serve(Tea())
    print(beverage)
    beverage = coffeeMachine.serve(Tea())
    print(beverage)
    beverage = coffeeMachine.serve(Tea())
    print(beverage)
    try:
        beverage = coffeeMachine.serve(Tea())
        print(beverage)
    except Exception as e:
        print(e)



if __name__ == '__main__':
   main()