import sys

def capital_city():

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

    for state_key, state_value in states.items():
        if sys.argv[1] == state_key:
            for capital_key, capital_value in capital_cities.items():
                if state_value == capital_key:
                    print(capital_value)
                    return

    print("Unknown state")

if __name__ == '__main__':
    capital_city()