class Intern:
    def __init__(self, name = None):
        self.name = name if name is not None else "My name? I'm nobody, an intern, I have no name"
    
    def __str__(self):
        return self.name

    class Coffee:
        def __str__(self):
            return "This is the worst coffee you ever tasted"

    def work(self):
        raise Exception("I'm just an intern, I can't do that...")

    def make_coffee(self):
        return self.Coffee()


def main():
    intern1 = Intern()
    intern2 = Intern("Mark")

    print("Intern1's name is:", intern1)
    print("Intern2's name is:", intern2)

    coffee = intern2.make_coffee()

    print("Intern2's coffee:", coffee)

    try:
        intern1.work()
    except Exception as error:
        print("Exception message:", error)


if __name__ == '__main__':
   main()