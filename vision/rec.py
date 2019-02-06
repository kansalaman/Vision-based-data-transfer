import cv2
import time
import numpy as np



if __name__ == '__main__':

    #  bits

    m1 = None
    m2 = None
    x = None  # Current bit

    # frames

    r = None
    classes = ["Black", "Red", "Green", "Blue"]
    prev_class = 0
    next_class = None
    ct = 0
    cts = 0
    cap = cv2.VideoCapture(0)

    # State variables

    flag = 1
    ts = 0

    while True:
        # Capture frame
        ret, frame = cap.read()
        if flag:
            r = cv2.selectROI(frame)
            flag = 0
        roi = frame[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]

        # Perform operations on the frame

         # Display the frame

        mean_int = cv2.mean(roi)
        if np.linalg.norm(mean_int) < 150:
            next_class = 0
            print("Black")
        elif np.linalg.norm(mean_int[:2]) < mean_int[2]:
            next_class = 1
            print("Red")
        elif np.linalg.norm(mean_int[1:3]) < mean_int[0]:
            next_class = 2
            print("Blue")
        else:
            next_class = 3
            print("Green")

        if not ts:
            if prev_class == 0:
                if next_class == 1:
                    print("Transmission started")
                    m1 = "1"
                    ts = 1
                if next_class == 2:
                    print("Transmission started")
                    m1 = "0"
                    ts = 1
        else:
            if prev_class == 3 and next_class == 1:
                m1 = m1 + "1"
            elif prev_class == 3 and next_class == 2:
                m1 = m1 + "0"
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        elif ct > 10:
            break
        if prev_class == 1 and next_class == 2:
            print(m1[:-1])

            break

        prev_class = next_class

    # When everything done, release the capture

    cap.release()
    cv2.destroyAllWindows()