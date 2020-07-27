import cv2
import matplotlib.pyplot as plt

img = cv2.imread("nature_edge.png")
histb = cv2.calcHist([img], [0], None, [256], [0, 250])
histg = cv2.calcHist([img], [1], None, [256], [0, 250])
histr = cv2.calcHist([img], [2], None, [256], [0, 250])
plt.subplot(131),plt.plot(histb),plt.title('Blue')
plt.subplot(132),plt.plot(histg),plt.title('Green')
plt.subplot(133),plt.plot(histr),plt.title('Red')
plt.show()