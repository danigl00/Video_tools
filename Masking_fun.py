import cv2
import numpy as np

COORDINATES = []

def draw_rectangle(image, coordinates):
    start_point = coordinates[0]
    width = coordinates[1][0] - start_point[0]
    height = coordinates[2][1] - start_point[1]
    end_point = (start_point[0] + width, start_point[1] + height)
    cv2.rectangle(image, start_point, end_point, (0, 255, 0), 2)
    cv2.putText(image, "*", start_point, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1)

    return start_point, end_point

def get_coordinates(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        COORDINATES.append((x, y))
        if len(COORDINATES) == 3:
            global start_point, end_point
            image, original_image = param
            image = original_image.copy()
            start_point, end_point = draw_rectangle(image, COORDINATES)
            cv2.imshow('Image', image)
            COORDINATES.clear()

def obtain_roi(original_image):
    image = original_image.copy()
    cv2.imshow('Image', image)
    cv2.setMouseCallback('Image', get_coordinates, [image, original_image])
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return start_point, end_point

def mask_roi(im2, start_point, end_point):
    image = im2.copy()
    black_image = np.zeros_like(image)
    # Create a mask with the ROI
    mask = np.zeros_like(image, dtype=np.uint8)
    cv2.rectangle(mask, start_point, end_point, (255, 255, 255), -1)
    # Use the mask to only show the ROI on the black image
    masked_image = cv2.bitwise_and(image, mask)
    masked_image += cv2.bitwise_and(black_image, cv2.bitwise_not(mask))
    return masked_image
