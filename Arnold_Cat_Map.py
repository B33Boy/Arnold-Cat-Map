# Author: Abhi Patel
# Date: 12/25/17
# Purpose: To implement an algorithm of Arnold's Cat Map.


import cv2
import numpy as np

def run():
    img = cv2.imread('img/dexter.png')

    for i in range (1,26):
        img = transform(img, i)

def transform(img, num):

    rows, cols, ch = img.shape
    if (rows == cols):
        n = rows
        img2 = np.zeros([rows, cols, ch])

        for x in range(0, rows):
            for y in range(0, cols):

                img2[x][y] = img[(x+y)%n][(x+2*y)%n]

        cv2.imwrite("img/iteration" + str(num) + ".jpg", img2)
        return img2

    else:
        print("The image is not square.")


if __name__ == "__main__":
    run()