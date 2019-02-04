import cv2
import time

def transmit(msg):
    for i in range(len(msg)):
        x = msg[-(i + 1)]
        if x == '1':
            pass
            display(1)
        else:
            pass
            display(0)
        display("Green")
        cv2.waitKey(200)

def display(col):
    global red_img
    global blue_img
    global green_img
    global win
    cv2.namedWindow('display', cv2.WINDOW_FULLSCREEN)
    if col == 1:
        cv2.imshow('display', red_img)
        cv2.waitKey(1000)
        print("Displaying red")
    elif col == 0:
        cv2.imshow('display', blue_img)
        cv2.waitKey(1000)
        print("Displaying blue")
    else:
        cv2.imshow('display', green_img)
        cv2.waitKey(500)

if __name__ == '__main__':

    red_img = cv2.imread("red.jpg")
    blue_img = cv2.imread("blue.jpg")
    green_img = cv2.imread("green.jpg")
    transmit("111")

