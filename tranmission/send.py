import cv2
import time
import numpy as np

red_img = [255, 0, 0]

def encode(message, pos1, pos2):
    pass

def transmit(msg):
    pass

if __name__ == '__main__':

    # first message
    m1 = input("Enter first message to be sent: ")
    p11 = input("Position of first error in first message: ")
    p12 = input("Position of second error in first message: ")


    # second message
    m2 = input("Enter first message to be sent")
    p21 = input("Position of first error in second message: ")
    p22 = input("Position of second error in second message: ")


    enc1 = encode(m1, p11, p22)
    transmit(enc1)

    # transmit separation

    enc2 = encode(m2, p21, p22)
    transmit(enc2)