import cv2, skimage
import numpy as np
import matplotlib.pyplot as plt
from skimage.segmentation import slic
from skimage.color import label2rgb

img = cv2.imread("nature.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Blurring the image
blur = cv2.blur(img, (15,15))

# Gaussian Blur on image
gblur = cv2.GaussianBlur(img,(15,15),0)

#Edge detection
edge = cv2.Canny(img, 300, 300)
plt.imshow(edge)
plt.show()

#SuperPixel - SLIC
seg = skimage.segmentation.slic(img, n_segments=300)
spxl = label2rgb(seg, img, kind='avg')

#Colour Skewed Superpixel
# Rotating hue by 180
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hsv[:,:,0] = (hsv[:,:,0] - 180)%180
h_cng_img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
# SuperPixel - SLIC
seg = skimage.segmentation.slic(h_cng_img, n_segments=300)
spxl_skwd = label2rgb(seg, h_cng_img, kind='avg')

# Plotting the image
# plt.subplot(321),plt.imshow(img),plt.title('Original')
# plt.xticks([]), plt.yticks([])
# plt.subplot(322),plt.imshow(blur),plt.title('Blurred')
# plt.xticks([]), plt.yticks([])
# plt.subplot(323),plt.imshow(gblur),plt.title('Gaussian Blur')
# plt.xticks([]), plt.yticks([])
# plt.subplot(324),plt.imshow(edge),plt.title('Edge')
# plt.xticks([]), plt.yticks([])
# plt.subplot(325),plt.imshow(spxl),plt.title('Superpixel')
# plt.xticks([]), plt.yticks([])
# plt.subplot(326),plt.imshow(spxl_skwd),plt.title('Colour Skewed Superpixel')
# plt.xticks([]), plt.yticks([])
# plt.show()