import numpy as np
import cv2
import requests

url = "http://192.168.1.134:8080/shot.jpg"

def get_image(url):
    imgResp = requests.get(url)
    imgNp = np.array(bytearray(imgResp.content),dtype = np.uint8)
    img = cv2.imdecode(imgNp,-1)
    return img
