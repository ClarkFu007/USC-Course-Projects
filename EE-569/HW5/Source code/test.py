import tensorflow as tf
import cv2


image = cv2.imread('landscape.jpg')
cv2.namedWindow("Image")
cv2.imshow("Image", image)
cv2.waitKey(0)

print(tf.__version__)