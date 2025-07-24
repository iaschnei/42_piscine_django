import sys, antigravity

def main():

    if len(sys.argv) != 4:
        print("Please input thses arguments : lat, long, date + dow jones such as '2005-05-26-10458.68' ")
        sys.exit()
    
    try:
        lat = float(sys.argv[1])
        lon = float(sys.argv[2])
    except ValueError:
        print("Latitude and Longitude must be valid floats.")
        sys.exit()

    try:
        date_dow = sys.argv[3].encode()
    except:
        print("Date_dow (arg 3) must be a valid string")
        sys.exit()
    
    antigravity.geohash(lat, lon, date_dow)
    
if __name__ == '__main__':
    main()
