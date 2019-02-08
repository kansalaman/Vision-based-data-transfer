import cv2
import time
import numpy as np
from fec import encode, decode


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


def start():
    cv2.namedWindow('display', cv2.WINDOW_FULLSCREEN)
    cv2.imshow('display', black_img)
    cv2.waitKey(10000)
    print("Displaying black")


def sep():
    cv2.namedWindow('display', cv2.WINDOW_FULLSCREEN)
    cv2.imshow('display', red_img)
    cv2.waitKey(1000)
    cv2.imshow('display', blue_img)
    cv2.waitKey(1000)
    print("Displaying sep character")

def black():
    cv2.namedWindow('display', cv2.WINDOW_FULLSCREEN)
    cv2.imshow('display', black_img)
    cv2.waitKey(3000)
    print("Displaying black")


def end():
    cv2.namedWindow('display', cv2.WINDOW_FULLSCREEN)
    cv2.imshow('display', blue_img)
    cv2.waitKey(1000)
    cv2.imshow('display', red_img)
    cv2.waitKey(1000)
    print("Displaying end character")


def encode(message, pos1, pos2):
    pass


if __name__ == '__main__':
    # Load images
    red_img = cv2.imread("red.jpg")
    blue_img = cv2.imread("blue.jpg")
    green_img = cv2.imread("green.jpg")
    black_img = np.zeros(red_img.shape)

    # first message
    m1 = input("Enter first message to be sent: ")
    p11 = input("Position of first error in first message: ")
    p12 = input("Position of second error in first message: ")

    # second message
    m2 = input("Enter first message to be sent")
    p21 = input("Position of first error in second message: ")
    p22 = input("Position of second error in second message: ")

    # encode messages

    enc1 = encode(m1, p11, p22)
    enc2 = encode(m2, p21, p22)

    start()
    transmit(enc1)
    sep()  # transmit separation
    transmit(enc2)
    end()
