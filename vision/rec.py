import cv2
import time

if __name__ == '__main__':

    #  bits

    m1 = None
    m2 = None
    x = None  # Current bit

    # frames

    r = None
    classes = ["Black", "Red", "Green", "Blue"]
    prev_class = None
    Next_class = None

    cap = cv2.VideoCapture(0)

    flag = 1
    while True:
        # Capture frame
        ret, frame = cap.read()
        if flag:
            r = cv2.selectROI(frame)
            flag = 0
        roi = frame[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]

        # Perform operations on the frame


         # Display the frame
        time.sleep(0.5)
        mean_int = cv2.mean(roi)

        print(mean_int)

        cv2.imshow('frame', roi)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()