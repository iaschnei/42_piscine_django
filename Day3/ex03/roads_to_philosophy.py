from bs4 import BeautifulSoup
import requests
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage : python3 request_wikipedia.py [xyz]")
        sys.exit()

    roads_to_philosophy = []

    road_to_philo(sys.argv[1], sys.argv[1], roads_to_philosophy)

def road_to_philo(initial_target, target, rtp):

    if target == "Philosophy":
        print(f"{len(rtp)} roads from {initial_target} to philosophy")
        sys.exit()

    if target in rtp:
        print("It leads to an infinite loop !")
        sys.exit()

    print(f"Visiting: {target}")
    rtp.append(target)

    request_str = f"https://en.wikipedia.org/wiki/{target}"

    # Requests handles redirects on its own
    r = requests.get(request_str) 

    if r.status_code != 200:
        print("Request failed")
        sys.exit()

    rtp.append(target)
    
    content = r.text

    soup = BeautifulSoup(content, 'html.parser')
    p_tags = soup.find_all('p')
    for paragraph in p_tags:
        first_link = paragraph.find('a', href=True)
        if first_link:
            href = first_link['href']
            if href.startswith('/wiki/') and not href.startswith('/wiki/Help:'):
                new_target = href[len('/wiki/'):]
                return road_to_philo(initial_target, new_target, rtp)

    print("It leads to a dead end!")
    sys.exit()

if __name__ == '__main__':
    main()