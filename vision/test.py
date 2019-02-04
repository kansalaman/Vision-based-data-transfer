import cv2
import time

red_img = cv2.imread("red.jpg")
blue_img = cv2.imread("blue.jpg")
green_img = cv2.imread("green.jpg")


cv2.imshow("Display", red_img)
cv2.waitKey(3000)
cv2.imshow("Display", green_img)
cv2.waitKey(0)
cv2.imshow("Display", blue_img)
cv2.waitKey(0)