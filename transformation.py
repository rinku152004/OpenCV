# # this code demonstrates image pyramids and edge detection using the Canny algorithm in OpenCV. It reads an image in grayscale, creates
# # a lower resolution version of the image using pyrDown, and then creates a higher resolution version using pyrUp. The original image and 
# # the processed images are displayed in separate windows. Additionally, it applies the Canny edge detection algorithm to the original 
# # image and displays the edges in a subplot alongside the original image using Matplotlib.
# import numpy as np
# import cv2 as cv
# from matplotlib import pyplot as plt

# img = cv.imread('images/roi.jpg', cv.IMREAD_GRAYSCALE)
# assert img is not None, "file could not be read, check with os.path.exists()"
# higher_reso = img
# lower_reso = cv.pyrDown(higher_reso)
# higher_reso2 = cv.pyrUp(lower_reso)
# # cv.imshow('image',lower_reso)
# cv.imshow('image',higher_reso2)
# cv.waitKey(0)
# edges = cv.Canny(img,100,200)

# plt.subplot(121),plt.imshow(img,cmap = 'gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(edges,cmap = 'gray')
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

# plt.show()












# import cv2 as cv
# import numpy as np
# # this code demonstrates various morphological transformations in OpenCV, such as erosion, dilation, opening, closing, gradient, tophat, and blackhat.
# # It reads an image in grayscale, applies a morphological operation using a kernel, and displays the result in a window.
# # img = cv.imread('closing.webp', cv.IMREAD_GRAYSCALE)
# img=cv.imread('opening.webp', cv.IMREAD_GRAYSCALE)
# assert img is not None, "file could not be read, check with os.path.exists()"
# # cv.getStructuringElement(cv.MORPH_RECT,(5,5))
# kernel = np.ones((5,5),np.uint8)
# # erosion = cv.erode(img,kernel,iterations = 1)
# # cv.imshow('image',erosion)

# # delation = cv.dilate(img,kernel,iterations = 1)
# # cv.imshow('image',delation)

# # opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
# # cv.imshow('image',opening)

# # closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
# # cv.imshow('image',closing)

# gradiant = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)
# cv.imshow('image',gradiant)

# # tophat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)
# # cv.imshow('image',tophat)

# # blackhat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)
# # cv.imshow('image',blackhat)

# cv.waitKey(0)
# cv.destroyAllWindows()



# # # Rectangular Kernel
# # >>> cv.getStructuringElement(cv.MORPH_RECT,(5,5))
# # array([[1, 1, 1, 1, 1],
# #        [1, 1, 1, 1, 1],
# #        [1, 1, 1, 1, 1],
# #        [1, 1, 1, 1, 1],
# #        [1, 1, 1, 1, 1]], dtype=uint8)

# # # Elliptical Kernel
# # >>> cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5))
# # array([[0, 0, 1, 0, 0],
# #        [1, 1, 1, 1, 1],
# #        [1, 1, 1, 1, 1],
# #        [1, 1, 1, 1, 1],
# #        [0, 0, 1, 0, 0]], dtype=uint8)

# # # Cross-shaped Kernel
# # >>> cv.getStructuringElement(cv.MORPH_CROSS,(5,5))
# # array([[0, 0, 1, 0, 0],
# #        [0, 0, 1, 0, 0],
# #        [1, 1, 1, 1, 1],
# #        [0, 0, 1, 0, 0],
# #        [0, 0, 1, 0, 0]], dtype=uint8)

# # # Diamond-shaped Kernel
# # >>> cv.getStructuringElement(cv.MORPH_DIAMOND,(5,5))
# # array([[0, 0, 1, 0, 0],
# #        [0, 1, 1, 1, 0],
# #        [1, 1, 1, 1, 1],
# #        [0, 1, 1, 1, 0],
# #        [0, 0, 1, 0, 0]], dtype=uint8)


# import numpy as np
# import cv2 as cv
# from matplotlib import pyplot as plt
# # this code demonstrates edge detection using the Laplacian and Sobel operators in OpenCV. It reads an image in grayscale, applies the 
# # Laplacian operator to detect edges, and applies the Sobel operator in both x and y directions to detect horizontal and vertical edges, 
# # respectively. The original image, Laplacian result, and Sobel results are displayed in a 2x2 grid using Matplotlib.
# img = cv.imread('images/ml.jpg', cv.IMREAD_GRAYSCALE)
# assert img is not None, "file could not be read, check with os.path.exists()"

# laplacian = cv.Laplacian(img,cv.CV_64F)
# sobelx = cv.Sobel(img,cv.CV_64F,1,0,ksize=5)
# sobely = cv.Sobel(img,cv.CV_64F,0,1,ksize=5)

# plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
# plt.title('Original'), plt.xticks([]), plt.yticks([])
# plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
# plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
# plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
# plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
# plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
# plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

# plt.show()


# import numpy as np
# import cv2 as cv
# from matplotlib import pyplot as plt
# # this code demonstrates the difference between using the Sobel operator with an output data type of CV_8U and CV_64F in OpenCV. It reads 
# # an image in color, applies the Sobel operator to detect edges in the x direction, and displays the original image, the result of the 
# # Sobel operator with CV_8U, and the result of the Sobel operator with CV_64F (after taking the absolute value and converting to CV_8U)
# # in a 1x3 grid using Matplotlib.
# img = cv.imread('images/starry_night.png', cv.IMREAD_COLOR_RGB)
# assert img is not None, "file could not be read, check with os.path.exists()"

# # Output dtype = cv.CV_8U
# sobelx8u = cv.Sobel(img,cv.CV_8U,1,0,ksize=5)

# # Output dtype = cv.CV_64F. Then take its absolute and convert to cv.CV_8U
# sobelx64f = cv.Sobel(img,cv.CV_64F,1,0,ksize=5)
# abs_sobel64f = np.absolute(sobelx64f)
# sobel_8u = np.uint8(abs_sobel64f)

# plt.subplot(1,3,1),plt.imshow(img,cmap = 'gray')
# plt.title('Original'), plt.xticks([]), plt.yticks([])
# plt.subplot(1,3,2),plt.imshow(sobelx8u,cmap = 'gray')
# plt.title('Sobel CV_8U'), plt.xticks([]), plt.yticks([])
# plt.subplot(1,3,3),plt.imshow(sobel_8u,cmap = 'gray')
# plt.title('Sobel abs(CV_64F)'), plt.xticks([]), plt.yticks([])

# plt.show()





# this code demonstrates image blending using pyramid blending in OpenCV. It reads two images, generates Gaussian and Laplacian pyramids for both 
# images, combines the left half of one image with the right half of the other image at each level of the Laplacian pyramids, and then reconstructs the blended 
# image from the combined pyramids. The final blended image and a direct blend (without pyramids) are saved to files.
import cv2 as cv
import numpy as np


# apple = cv.imread('images/apple.png')
# orange = cv.imread('images/orange.png')

# Read images
apple = cv.imread('images/apple.png')
orange = cv.imread('images/orange.png')

# Resize to same size
apple = cv.resize(apple,(512,512))
orange = cv.resize(orange,(512,512))

# ---------------------------
# 1. Gaussian Pyramid
# ---------------------------
gpA = [apple]
gpO = [orange]

for i in range(6):
    apple = cv.pyrDown(apple)
    orange = cv.pyrDown(orange)
    gpA.append(apple)
    gpO.append(orange)

# ---------------------------
# 2. Laplacian Pyramid
# ---------------------------
lpA = [gpA[5]]
for i in range(5,0,-1):
    GE = cv.pyrUp(gpA[i])
    GE = cv.resize(GE,(gpA[i-1].shape[1], gpA[i-1].shape[0]))
    L = cv.subtract(gpA[i-1],GE)
    lpA.append(L)

lpO = [gpO[5]]
for i in range(5,0,-1):
    GE = cv.pyrUp(gpO[i])
    GE = cv.resize(GE,(gpO[i-1].shape[1], gpO[i-1].shape[0]))
    L = cv.subtract(gpO[i-1],GE)
    lpO.append(L)

# ---------------------------
# 3. Combine Left & Right
# ---------------------------
LS = []
for la, lo in zip(lpA,lpO):
    rows, cols, ch = la.shape
    ls = np.hstack((la[:,0:cols//2], lo[:,cols//2:]))
    LS.append(ls)

# ---------------------------
# 4. Reconstruct Image
# ---------------------------
ls_ = LS[0]
for i in range(1,6):
    ls_ = cv.pyrUp(ls_)
    ls_ = cv.resize(ls_,(LS[i].shape[1],LS[i].shape[0]))
    ls_ = cv.add(ls_,LS[i])

# Normal direct blending (for comparison)
real = np.hstack((gpA[0][:,:256], gpO[0][:,256:]))

# Show results
cv.imshow("Pyramid Blending", ls_)
cv.imshow("Direct Blending", real)

cv.waitKey(0)
cv.destroyAllWindows()