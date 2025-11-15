import cv2

image = cv2.imread(r"image_resizer_project\m6YhOg.jpg")

# scale_percent = 50 means reduce size 50%
scale_percent = 50  

width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)

resized = cv2.resize(image, (width, height))

cv2.imshow("Resized", resized)
cv2.waitKey(0)
