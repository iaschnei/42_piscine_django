import dewiki
import requests
import json
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage : python3 request_wikipedia.py [xyz]")
        sys.exit()

    get_content(sys.argv[1])

def get_content(target):

    params = {
        "action": "raw",
        "title": target,
    }

    request_str = f"https://fr.wikipedia.org/w/index.php"

    r = requests.get(request_str, params=params)

    if r.status_code != 200:
        print("Request failed")
        sys.exit()
    
    content = r.text

    # Check if the page we want to access is a redirect to another
    if content.upper().startswith("#REDIRECT"):
        start = content.find("[[") + 2
        end = content.find("]]", start)
        if start > 1 and end > start:
            new_target = content[start:end]
            print(f"Redirected to: {new_target}")
            return get_content(new_target)

    clean_content = dewiki.from_string(content)

    target = target.replace(" ", "_")
    f = open(f"{target}.wiki", "w")
    f.write(clean_content)

if __name__ == '__main__':
    main()