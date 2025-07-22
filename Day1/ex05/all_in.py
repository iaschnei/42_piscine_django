import sys

def all_in():

    if len(sys.argv) != 2:
        return 

    input = sys.argv[1].split(',')

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

    found = False

    for entry in input:
        if (entry.strip() == ""):
            continue
        for capital_key, capital_value in capital_cities.items():
            if entry.strip().lower() == capital_value.lower():
                for state_key, state_value in states.items():
                    if capital_key == state_value:
                        print(capital_value, "is the capital of", state_key)
                        found = True
        for state_key, state_value in states.items():
            if entry.strip().lower() == state_key.lower():
                for capital_key, capital_value in capital_cities.items():
                    if state_value == capital_key:
                        print(capital_value, "is the capital of", state_key)
                        found = True
        if (found == False):
            print(entry.strip(), "is neither a capital city nor a state")
        found = False

if __name__ == '__main__':
    all_in()