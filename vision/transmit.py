import cv2
import time

def transmission(msg):
    for i in range(len(msg)):
        x = msg(-(i + 1))
        if x == '1':
            pass
            display(1)
        else:
            pass
            display(0)
        time.sleep(0.5)
        display("Green")
        display(0.2)
#
#
# red_img = cv2.imread("red.jpg")
# blue_img = cv2.imread("blue.jpg")
# green_img = cv2.imread("green.jpg")
#
# win = cv2.namedWindow("display", cv2.WINDOW_FULLSCREEN)


def display(col):
    global red_img
    global blue_img
    global green_img
    global win
    # cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
    # cv2.setWindowProperty("window", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    if col == 1:
        cv2.imshow('display', red_img)
        print("Displaying red")
    elif col == 0:
        cv2.imshow('display', blue_img)
        print("Displaying blue")
    else:
        cv2.imshow('display', green_img)


if __name__ == '__main__':

    red_img = cv2.imread("red.jpg")
    blue_img = cv2.imread("blue.jpg")
    green_img = cv2.imread("green.jpg")

    cv2.namedWindow('display', cv2.WINDOW_FULLSCREEN)

    cv2.imread("ref.jpg")
    display(1)
    time.sleep(1)
    display("avnjasdn")
    time.sleep(1)
    display(0)
    time.sleep(1)
    display("nakjnbv")
    time.sleep(1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


