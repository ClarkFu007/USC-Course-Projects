import cv2
from cv2 import dnn_superres


# Create an SR object
sr = dnn_superres.DnnSuperResImpl_create()

# Read image
image = cv2.imread("Yao Fu.jpg")

# Read the desired model
path = "FSRCNN_x2.pb"
sr.readModel(path)

# Set the desired model and scale to get correct pre- and post-processing
sr.setModel("edsr", 3)

# Upscale the image
result = sr.upsample(image)

# Save the image
cv2.imwrite("new Yao Fu.jpg", result)


cv2.namedWindow("output image", cv2.WINDOW_AUTOSIZE)
cv2.imshow("output image", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
