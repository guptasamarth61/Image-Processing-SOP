import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("nature_edge.png")
# img_double = cv2.normalize(img.astype('float'), None, 0.0, 1.0, cv2.NORM_MINMAX)
rows = img.shape[0]
cols = img.shape[1]


#diagonal
def diagonal():
    initxy = []
    incrxy = []
    for i in range(0,rows-1, 50):
        for j in range(0, cols-1, 50):
            initxy.append(np.average(img[i][j]))
            incrxy.append(np.average(img[i+1][j+1]))
    corrd = np.corrcoef(initxy, incrxy)[0][1]
    print(corrd)
    plt.scatter(initxy, incrxy)
    plt.show()


#horizontal
def horizontal():
    initxy = []
    incrxy = []
    for i in range(0,rows-1, 50):
        for j in range(0, cols-1, 50):
            initxy.append(np.average(img[i][j]))
            incrxy.append(np.average(img[i+1][j]))
    corrd = np.corrcoef(initxy, incrxy)[0][1]
    print(corrd)
    plt.scatter(initxy, incrxy)
    plt.show()


# vertical
def vertical():
    initxy = []
    incrxy = []
    for i in range(0,rows-1, 50):
        for j in range(0, cols-1, 50):
            initxy.append(np.average(img[i][j]))
            incrxy.append(np.average(img[i][j+1]))
    corrd = np.corrcoef(initxy, incrxy)[0][1]
    print(corrd)
    plt.scatter(initxy, incrxy)
    plt.show()

diagonal()
horizontal()
vertical()