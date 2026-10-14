import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("example1.jpeg")
b,g,r = cv.split(img)

bN = 255 - b
gN = 255 - g
rN = 255 - r


plt.figure()
plt.subplot(131)
plt.imshow(bN, cmap = 'gray')
plt.title('Blue Negative')

plt.subplot(132)
plt.imshow(gN, cmap = 'gray')
plt.title('Green Negative')

plt.subplot(133)
plt.imshow(rN, cmap = 'gray')
plt.title('Red Negative')

plt.show()
