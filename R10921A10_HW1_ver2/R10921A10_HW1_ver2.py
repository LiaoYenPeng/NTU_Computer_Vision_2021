import cv2
import numpy as np

def upside_down(img):
    img_output = np.zeros(img.shape, int)
    for i in range(img.shape[0]):
        img_output[i, :] = img[img.shape[0] - i - 1, :]
    return img_output

def right_side_left(img):
    img_output = np.zeros(img.shape, int)
    for j in range(img.shape[1]):
        img_output[:, j] = img[:, img.shape[1] - j - 1]
    return img_output

def diagonally_flip(img):
    img_output = np.zeros(img.shape, int)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img_output[i, j] = img[img.shape[0] - i - 1, img.shape[1] - j - 1]
    return img_output

def rotate45(img, angle = -45, center = None, scale = 1.0):
    (h, w) = img.shape[:2]
    if center is None:
        center = (w / 2, h / 2)
    M = cv2.getRotationMatrix2D(center, angle, scale)
    img_output = cv2.warpAffine(img, M, (w, h))
    return img_output

def shrink_half(img):
    img_output = cv2.resize(img,(256,256))
    return img_output

def binarize(img):
    th, img_output = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)
    return img_output

img = cv2.imread("lena.bmp")    
img_output = upside_down(img)
cv2.imwrite('upside_down.jpg', img_output)
img_output = right_side_left(img)
cv2.imwrite('right_side_left.jpg', img_output)
img_output = diagonally_flip(img)
cv2.imwrite('diagonally_flip.jpg', img_output)
img_output = rotate45(img)
cv2.imwrite('rotate45.jpg', img_output)
img_output = shrink_half(img)
cv2.imwrite('shrink_half.jpg', img_output)
img_output = binarize(img)
cv2.imwrite('binarize.jpg', img_output)
