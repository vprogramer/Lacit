import cv2
import scipy
import matplotlib as plt
import numpy as np

#Sobel method
def round_one(photo = "image/rr.bmp"):
    img = cv2.imread(photo)
    img = cv2.resize(img, (512, 1050))
    img = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    laplacian = cv2.Laplacian(gray,cv2.CV_64F)
    cv2.imshow("lapla", laplacian)
    grad_x = cv2.Sobel(gray, cv2.CV_16S, 1, 0, ksize=3, scale=1, delta=0, borderType=cv2.BORDER_DEFAULT)
    grad_y = cv2.Sobel(gray, cv2.CV_16S, 0, 1, ksize=3, scale=1, delta=0, borderType=cv2.BORDER_DEFAULT)
    abs_grad_x = cv2.convertScaleAbs(grad_x)
    abs_grad_y = cv2.convertScaleAbs(grad_y)

    grad = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)

    cv2.imshow("sobel", grad)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
# findContours
def round_two(photo = "image/rr.bmp"):
    img = cv2.imread(photo)
    img = cv2.resize(img, (512, 1050))
    img = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)

    #yellow
    # hsv_min = np.array((5, 88, 31), np.uint8)
    # hsv_max = np.array((26, 169, 111), np.uint8)

    #broun
    # hsv_min = np.array((12, 43, 171), np.uint8)
    # hsv_max = np.array((30, 137, 255), np.uint8)

    hsv_min = np.array((0, 43, 20), np.uint8)
    hsv_max = np.array((30, 169, 255), np.uint8)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    thresh = cv2.inRange(hsv, hsv_min, hsv_max)
    cv2.imshow('thresh', thresh)

    contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    max_len_contours = 0
    index_max_contour = 0
    for i in range(len(contours)):
        if max_len_contours < len(contours[i]):
            max_len_contours = len(contours[i])
            index_max_contour = i

    cv2.drawContours(img, contours, index_max_contour, (255, 0, 0), 3, cv2.LINE_AA, hierarchy, 1)
    cv2.imshow('contours', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

#round_one()
round_two("image/rr_13.bmp")
