import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('road.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blur, 50, 150)

height, width, _ = img.shape
triangle = np.array([[(100, height), (475, 325), (width, height)]])

mask = np.zeros_like(edges)
mask = cv2.fillPoly(mask, triangle, 255)
mask = cv2.bitwise_and(edges, mask)

lines = cv2.HoughLinesP(mask, 1, np.pi/180, 100, minLineLength=50, maxLineGap=10)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

plt.imshow(img)
plt.show()