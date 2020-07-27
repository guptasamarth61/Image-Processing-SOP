import cv2, skimage
import matplotlib.pyplot as plt
from skimage.filters.rank import entropy
from skimage.morphology import disk
img = cv2.imread("nature_super_skewed.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
entrimg = entropy(gray, disk(10))
fig, ax = plt.subplots()
im = ax.imshow(entrimg,  cmap='viridis')
fig.colorbar(im)
plt.show()