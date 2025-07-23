import sys
import os
import re

settings = {}

#Split every line into a tuple
def parse_line(line):
    key, value  = line.split(" = ")
    value = value.strip('"')
    return (key, value)

def extract_settings():
    try:
        f = open("settings.py")
        content = f.read()
    except:
        print("Could not open or read settings file (settings.py)")
        sys.exit()
    content = content.split('\n')

    values = {}

    try:
        for line in content:
            value_tuple = parse_line(line)
            values[value_tuple[0]] = value_tuple[1]
    except:
        print("Values aren't properly formated in settings.py")
        sys.exit()

    return values

def replacer(matched_value):
    key = matched_value.group(1)  # -> this corresponds to regex match without the {}
    if key in settings:
        return settings[key]
    else:
        return "{" + key + "}"

def render():

    global settings

    if len(sys.argv) != 2:
        print("Please input a template file")
        sys.exit()

    settings = extract_settings()

    template_file = sys.argv[1]
    try:
        f = open(template_file)
        html_template = f.read()
    except:
        print("Could not open or read template file")
        sys.exit()

    result = re.sub(r"\{(\w+)\}", replacer, html_template)

    try:
        new_f = open("file.html", "w")
        new_f.write(result)
    except:
        print("Could not write in result file")


if __name__ == '__main__':
    render()