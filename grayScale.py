import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("images2.jpeg")
b,g,r = cv.split(img)

plt.figure()
plt.subplot(131)
plt.imshow(b, cmap='gray')
plt.title('blue')

plt.subplot(132)
plt.imshow(g, cmap='gray')
plt.title('green')

plt.subplot(133)
plt.imshow(r, cmap='gray')
plt.title('red')

plt.show()
