import nasapy
import os
from datetime import datetime
import urllib.request

API_KEY = "Put your NASA API KEY here"

def todays_image():
    nasa = nasapy.Nasa(key = API_KEY)
    d = datetime.today().strftime('%Y-%m-%d')
    apod = nasa.picture_of_the_day(date=d, hd=True)

    if (apod["media_type"] == "image"):
        if ("hdurl" in apod.keys()):
            title = d + "_" + apod["title"].replace(" ", "_").replace(":","_") + ".jpg"
            image_dir = "./Astro_Images"
            dir_res = os.path.exists(image_dir)
            if (dir_res == False):
                os.makedirs(image_dir)
            else:
                print("Directory already exists.\n")
            urllib.request.urlretrieve(url=apod["hdurl"], filename=os.path.join(image_dir, title))
        
            if("title" in apod.keys()):
                print(apod["title"])
                print("\n")
            if("explanation" in apod.keys()):
                print(apod["explanation"])

    else:
        print("Sorry, image not available.")

todays_image()
