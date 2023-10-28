import cv2
import numpy as np


def Subtract(image1_path, image2_path, image_output):
    # Read the PNG images using OpenCV
    image1 = cv2.imread(image1_path, cv2.IMREAD_GRAYSCALE)
    image2 = cv2.imread(image2_path, cv2.IMREAD_GRAYSCALE)

    # Ensure both images have the same shape
    image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

    # Convert images to NumPy arrays for manipulation
    image1_arr = np.array(image1, dtype=np.float32)
    image2_arr = np.array(image2, dtype=np.float32)

    # Perform subtraction
    result_arr = np.subtract(image2_arr, image1_arr)

    # Normalize the pixel values to the range [0, 255]
    result_arr = cv2.normalize(result_arr, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)

    # Save the resulting image
    cv2.imwrite(image_output, result_arr)

