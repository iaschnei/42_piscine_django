def my_sort():
    d = {
        'Hendrix' : '1942',
        'Allman' : '1946',
        'King' : '1925',
        'Clapton' : '1945',
        'Johnson' : '1911',
        'Berry' : '1926',
        'Vaughan' : '1954',
        'Cooder' : '1947',
        'Page' : '1944',
        'Richards' : '1943',
        'Hammett' : '1962',
        'Cobain' : '1967',
        'Garcia' : '1942',
        'Beck' : '1944',
        'Santana' : '1947',
        'Ramone' : '1948',
        'White' : '1975',
        'Frusciante': '1970',
        'Thompson' : '1949',
        'Burton' : '1939',
    }
    # Sort by names (we end up with a list of tuples we convert back to a dict):
    sorted_d_list = sorted(d.items())
    sorted_d = {}
    for key, value in sorted_d_list:
        sorted_d[key] = value
    
    # Sort by dates :
    sorted_d = sorted(sorted_d.items(), key=lambda item: item[1])

    for key, value in sorted_d:
        print(key)
    


if __name__ == '__main__':
    my_sort()