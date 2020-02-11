import cv2
import random
import numpy as np


#This function uses Sobel method to find border of an object.
def use_Sobel(photo="image/rr.bmp"):
    img = cv2.imread(photo)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    grad_x = cv2.Sobel(gray, cv2.CV_16S, 1, 0, ksize=3, scale=1, delta=0, borderType=cv2.BORDER_DEFAULT)
    grad_y = cv2.Sobel(gray, cv2.CV_16S, 0, 1, ksize=3, scale=1, delta=0, borderType=cv2.BORDER_DEFAULT)
    abs_grad_x = cv2.convertScaleAbs(grad_x)
    abs_grad_y = cv2.convertScaleAbs(grad_y)

    grad = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)

    cv2.imshow("sobel", grad)


# This function uses cv2.findContours to find border of an object.
def use_findContours(photo="image/rr.bmp"):
    img = cv2.imread(photo)

    # Settings for yellow skin.
    # hsv_min = np.array((5, 88, 31), np.uint8)
    # hsv_max = np.array((26, 169, 111), np.uint8)

    # Setting for brown skin.
    # hsv_min = np.array((12, 43, 171), np.uint8)
    # hsv_max = np.array((30, 137, 255), np.uint8)

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

    cv2.drawContours(img, contours, index_max_contour, (255, 0, 0), 3, cv2.LINE_AA, hierarchy, 1)
    cv2.imshow('contours', img)


if __name__ == "__main__":
    use_Sobel("image/rr_3.bmp")
    use_findContours("image/rr_13.bmp")
    cv2.waitKey(0)
    cv2.destroyAllWindows()


