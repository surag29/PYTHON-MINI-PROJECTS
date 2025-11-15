import cv2

image = cv2.imread(r"image_resizer_project\m6YhOg.jpg")


def resize_image(scale):
    scale = scale if scale > 0 else 1   # avoid zero division
    width = int(image.shape[1] * scale / 100)
    height = int(image.shape[0] * scale / 100)
    resized = cv2.resize(image, (width, height))
    cv2.imshow("Resized Image", resized)


cv2.namedWindow("Resized Image")


cv2.createTrackbar("Scale %", "Resized Image", 100, 300, resize_image)


resize_image(100)


cv2.waitKey(0)
cv2.destroyAllWindows()
