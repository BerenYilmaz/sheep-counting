import cv2 as cv
import matplotlib.pyplot as plt

image = cv.imread("images2.jpeg")

histGreen = cv.calcHist(image, [1], None, [256], [0, 256])
histRed = cv.calcHist(image, [2], None, [256], [0, 256])
histBlue = cv.calcHist(image, [0], None, [256], [0, 256])

histGreen /= histGreen.sum()
histRed /= histRed.sum()
histBlue /= histBlue.sum()

plt.figure()

plt.subplot(131)
plt.title("Grayscale Histogram Normalized Green")
plt.xlabel("Bins")
plt.ylabel(" Percentage of Pixels")
plt.plot(histGreen, color='g')
plt.xlim([0,256])

plt.subplot(132)
plt.title("Grayscale Histogram Normalized Red")
plt.xlabel("Bins")
plt.ylabel(" Percentage of Pixels")
plt.plot(histRed, color='r')
plt.xlim([0,256])

plt.subplot(133)
plt.title("Grayscale Histogram Normalized Blue")
plt.xlabel("Bins")
plt.ylabel(" Percentage of Pixels")
plt.plot(histBlue, color='b')
plt.xlim([0,256])

plt.show()
