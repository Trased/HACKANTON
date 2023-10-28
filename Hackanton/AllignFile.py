import cv2
import numpy as np

def Align(image1, image2, output):
    # Read the images
    img1 = cv2.imread(image1, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(image2, cv2.IMREAD_GRAYSCALE)

    # Apply some pre-processing if needed (e.g., denoising, normalization)

    # Use OpenCV's ORB (Oriented FAST and Rotated BRIEF) feature detector
    orb = cv2.ORB_create()

    # Find key points and descriptors in the images
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)

    # Create a brute-force matcher
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors
    matches = bf.match(des1, des2)

    # Sort matches based on distance
    matches = sorted(matches, key=lambda x: x.distance)

    # Extract location of keypoints in both images
    points1 = np.float32([kp1[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
    points2 = np.float32([kp2[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)

    # Compute the homography matrix
    H, _ = cv2.findHomography(points1, points2, cv2.RANSAC)

    # Use the homography matrix to align the images
    aligned_img = cv2.warpPerspective(img1, H, (img2.shape[1], img2.shape[0]))

    cv2.imwrite(output, aligned_img)
    return aligned_img
