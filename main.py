import nasapy
import os
from datetime import datetime
import urllib.request
import requests
from properties import API_KEY
import logging

logging.basicConfig(filename="log.log", encoding='utf-8', level=logging.DEBUG, \
                    format='%(asctime)s %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

def todays_image():
    try:
        nasa = nasapy.Nasa(key = API_KEY)
        d = datetime.today().strftime('%Y-%m-%d')
        apod = nasa.picture_of_the_day(date=d, hd=True)
    except requests.exceptions.HTTPError as err1:
        logging.info(f"{err1}. (Failed connection to the API, check the date and API Key for errors).")
    
    
    try:
        if (apod["media_type"] == "image"):
            if ("hdurl" in apod.keys()):
                title = d + "_" + apod["title"].replace(" ", "_").replace(":","_") + ".jpg"
                image_dir = "./Astro_Images"
                dir_res = os.path.exists(image_dir)
                if (dir_res == False):
                    os.makedirs(image_dir)
                urllib.request.urlretrieve(url=apod["hdurl"], filename=os.path.join(image_dir, title))
            
                if("title" in apod.keys()):
                    print(apod["title"])
                    print("\n")
                if("explanation" in apod.keys()):
                    print(apod["explanation"])
        else:
            logging.debug("Image not available.")
    except UnboundLocalError as err2:
        logging.info(f"{err2}. (Likely, the connection to the API failed).")
        

if __name__=="__main__":
    todays_image()
