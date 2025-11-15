import cv2

image = cv2.imread(r"image_resizer_project\m6YhOg.jpg")

resized_image = cv2.resize(image, (300, 300))


cv2.imshow("Original Image", image)


cv2.imshow("Resized Image", resized_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
