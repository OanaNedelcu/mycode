#!usr/bin/python3
import urllib.request
import json

NASAPI = "https://api.nasa.gov/planetary/apod?"

def main():
    with open("/home/student/nasa.creds") as mycreds:
        print(type(mycreds))
        nasacreds = mycreds.read()
    nasacreds = "api_key=" + nasacreds.strip("\n")
    apodurlobj = urllib.request.urlopen(NASAPI + nasacreds)
    print( apodurlobj)
    apodread = apodurlobj.read()
    apod = json.loads(apodread.decode("utf-8"))
    print("\nConverted Python data", apod)
    
    print(apod["title"] + "\n")
    print(apod["date"] + "\n")
    print(apod["explanation"] + "\n")
    print(apod["url"])
if __name__ == "__main__":
    main()
