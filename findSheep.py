import cv2 as cv

img = cv.imread("images2.jpeg", cv.IMREAD_GRAYSCALE)
template = cv.imread("template2.jpeg", cv.IMREAD_GRAYSCALE)

imgN = 255 - img

w, h = template.shape[ : :-1]

template_inv = 255 - template

img1 = cv.matchTemplate(img, template, cv.TM_CCOEFF_NORMED)
img2 = cv.matchTemplate(img, template_inv, cv.TM_CCOEFF_NORMED)

result = img1.copy()

for y in range(img2.shape[0]):
    for x in range(img2.shape[1]):
        if img2[y][x] > result[y][x]:
            result[y][x] = img2[y][x]

threshold = 0.5
candidates = []

for y in range(result.shape[0]):
    for x in range(result.shape[1]):
        if result[y][x] >= threshold:
            candidates.append((x,y))

def is_close(p1, p2, dist=25):
    return abs(p1[0] - p2[0]) < dist and abs(p1[1] - p2[1]) < dist

filtered = []

for c in candidates:
    keep = True

    for f in filtered:
        if is_close(c, f):
            keep = False

    if keep:
        filtered.append(c)

img_color = cv.cvtColor(img, cv.COLOR_GRAY2BGR)

for (x,y) in filtered:
    cv.rectangle(img_color, (x,y), (x + w, y + h), (0, 255, 0), 2)

print ("Koyun Sayısı ", len(filtered))

cv.imshow("original Image", img)
cv.imshow("Negative Image", imgN)
cv.imshow("Detection", img_color)

cv.waitKey(0)
cv.destroyAllWindows()
