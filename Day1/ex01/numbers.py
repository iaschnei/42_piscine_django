def number_read():
    f = open("numbers.txt")
    content = f.read()
    result = content.split(',')
    for num in result:
        print(num)

if __name__ == '__main__':
    number_read()