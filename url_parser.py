import sys
import requests
import re
import urllib.request


def findImagesFromUrl(url :str):


    req = requests.get(url)

    urls = re.findall('(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-?=%.]+', req.text)

    images_link = []
    for link in urls:

        if link.find("googleusercontent") != -1:
            images_link.append(link)

    return images_link




def download_imagesFromUrl():



    print("находим картинки")
    images_link = findImagesFromUrl("https://docs.google.com/document/d/1Jy5UKWF0KBeH12qiAkQfr85shWl9LB4P2Mj_AIlwk4Q/edit?usp=sharing")
    print("скачиваем с сайта")
    

    img_number = 0
    for imgLink in images_link:
        img_number = img_number + 1

        print(imgLink)

        urllib.request.urlretrieve(imgLink,f"download_img/img{img_number}.png")



