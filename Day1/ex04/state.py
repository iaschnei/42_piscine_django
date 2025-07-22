import sys

def state():

    if len(sys.argv) != 2:
        return 

    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

    for capital_key, capital_value in capital_cities.items():
        if sys.argv[1] == capital_value:
            for state_key, state_value in states.items():
                if capital_key == state_value:
                    print(state_key)
                    return

    print("Unknown capital city")

if __name__ == '__main__':
    state()