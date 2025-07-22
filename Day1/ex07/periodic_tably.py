import sys 

#Split every line into a dictionary 
def parse_line(line):
    name, rest = line.split(" = ")
    properties = {}
    for item in rest.split(", "):
        key, value = item.split(":")
        properties[key] = value
    properties["name"] = name
    return properties

def periodic_table():
    f = open("periodic_table.txt")
    content = f.read().split('\n')

    elements = [parse_line(line) for line in content]

    html = open("periodic_table.html", "a")
    html.write("<!DOCTYPE html>\n<html>\n<head>\n  <title>Periodic table</title>\n</head>\n<body>\n  <table>\n")
    html.write('  <table style="border-collapse: collapse;">\n')

    rows = []
    current_row = []
    last_position = 0


    # Create table structure
    for element in elements:
        position = int(element["position"])

        # If current row contains stuff and we need to set it on position 0, append a new row
        if position == 0 and current_row:
            rows.append(current_row)
            current_row = []

        # If there is a gap, add empty cells
        while len(current_row) < position:
            current_row.append(None)

        current_row.append(element)

    if current_row:
        rows.append(current_row)

    for row in rows:
        html.write("  <tr>\n")
        for element in row:
            if element is None:
                html.write('    <td></td>\n')
            else:
                html.write('    <td style="border: 1px solid black; padding: 10px;">\n')
                html.write(f'      <h4>{element["name"]}</h4>\n')
                html.write('      <ul>\n')
                html.write(f'        <li>No {element["number"]}</li>\n')
                html.write(f'        <li>{element["small"]}</li>\n')
                html.write(f'        <li>{element["molar"]}</li>\n')
                electrons = element["electron"].split()
                html.write(f'        <li>{" ".join(electrons)} electron{"s" if len(electrons) > 1 else ""}</li>\n')
                html.write('      </ul>\n')
                html.write('    </td>\n')
        html.write("  </tr>\n")



    html.write("  </table>\n</body>\n</html>\n")

if __name__ == '__main__':
    periodic_table()