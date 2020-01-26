import cv2
import numpy as np

image = cv2.imread('test_image.jpg')
lane_image = np.copy(image)
gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)

cv2.imshow('result', gray)

blur = cv2.GaussianBlur(gray, (5,5),0)
cv2.imshow('result1', blur)
cv2.waitKey(0)
