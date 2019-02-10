import encode
import decode
print(encode.encode('1001101',2,3))
print(decode.decode(encode.encode('100110100101',3,4)))
import cv2
x=cv2.imread('green.jpg')
print(x)