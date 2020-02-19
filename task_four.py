import cv2
import time
import json
import numpy as np
import glob
import socket
import pickle


# This function uses cv2.findContours to find border of an object.
def use_findContours(photo="image/rr.bmp"):
    img = cv2.imread(photo)
    hsv_min = np.array((0, 43, 20), np.uint8)
    hsv_max = np.array((30, 169, 255), np.uint8)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    thresh = cv2.inRange(hsv, hsv_min, hsv_max)
    contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    max_len_contours = 0
    index_max_contour = 0
    for i in range(len(contours)):
        if max_len_contours < len(contours[i]):
            max_len_contours = len(contours[i])
            index_max_contour = i

    return contours[index_max_contour]

#Get contours and write to JSON
def write_json(name_json = 'skin_contours.json'):
    path = glob.glob("image/*.bmp")
    all_skin_contours = []
    for i in path:
        all_skin_contours.append(use_findContours(i))
    skin_contours = []

    #Convert list(array) to list(list)
    for i in range(len(all_skin_contours)):
        skin_contours.append(all_skin_contours[i].tolist())

    dict_with_contours = dict(zip(path, skin_contours))

    #Write json
    with open(name_json,'w') as file:
        file.write(json.dumps(dict_with_contours))


if __name__ == "__main__":
    name_json = 'skin_contours.json'
    write_json(name_json)

    #Read JSON
    with open(name_json) as f:
        contours = json.load(f)

    #Connect to server
    sock = socket.socket()
    sock.connect(('localhost', 9092))
    sock.send(pickle.dumps(contours))
    sock.send(bytes(123))
    sock.close()

