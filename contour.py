# this code demonstrates how to find contours in an image, approximate them to polygons, identify 
# shapes, and filter contours by area using OpenCV in Python.

import cv2 as cv

img = cv.imread('images/contour.png')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
# for contour in contours:
cv.drawContours(img, contours, -1, (255, 0, 0), 3)
cv.imshow('Contours', img)
cv.waitKey(0)
# cv.destroyAllWindows()
    
# Approximate contours to polygons and identify shapes & draw them 
for contour in contours:
    approx = cv.approxPolyDP(contour, 0.01 * cv.arcLength(contour, True), True)
    corners = len(approx)
    print(f'Number of corners: {corners}')
    if corners == 3:
        shape = 'Triangle'
    elif corners == 4:
        shape = 'Quadrilateral'
    elif corners == 5:
        shape = 'Pentagon'
    elif corners == 6:
        shape = 'Hexagon'
    elif corners > 6:        
        shape = 'Circle'
    else:
        shape = 'Unknown'
    print(f'Shape: {shape}')
    cv.drawContours(img, [approx], -1, (255, 255, 0), 3)
    x=approx.ravel()[0]
    y=approx.ravel()[1]+20
    cv.putText(img, shape, (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 2)

cv.imshow('Contours', img)
cv.waitKey(0)
cv.destroyAllWindows()

# Filter contours by area and draw them
for contour in contours:

    area = cv.contourArea(contour)
    print(f'Contour area: {area}')
    if area > 100:
        cv.drawContours(img, [contour], -1, (255, 0, 0), 3)
        cv.imshow('Large Contours', img)
        cv.waitKey(0)

# Approximate contours to polygons and draw them 
for contour in contours:
    epsilon = 0.01 * cv.arcLength(contour, True)
    approx = cv.approxPolyDP(contour, epsilon, True)
    if len(approx) == 4:
        cv.drawContours(img, [approx], -1, (0, 0, 255), 3)
        cv.imshow('Approximated Contours', img)
        cv.waitKey(0)
cv.destroyAllWindows()
