"""
    EYW II Unit 3 Exploring Images

    File: Images_10_Greyscale_Trackbars.py
    Date: 11/7/17
    Author: Alfredo Salazar
    Version: 1.0

"""

import cv2
import numpy as np
import os
import os.path
import sys

print "\nAvailable image filenames: "
path = "images"
dirs = os.listdir(path)
for file in dirs:
    print file

# Ask for name of image
print ""
imgname_entry_valid = False
while not imgname_entry_valid:
    imgname = raw_input("Filename of image? ")

    if os.path.isfile("images/" + imgname):
        imgname_entry_valid = True
    else:
        print "Image filename was incorrect, try again.\n"
print ""

# Read in the image, but in greyscale, to a variable
gImg = cv2.imread("images/" + imgname, 0)

# Change the greyscale image to a 3 channel image
gCImg = cv2.cvtColor(gImg, cv2.COLOR_GRAY2BGR)

def nothing(x):
    pass

# Create a new window to display trackbars
cv2.namedWindow("Color Trackbars")
cv2.resizeWindow("Color Trackbars", 500, 900)

# Create nine trackbars (BGR values for each color) that can
# be used to adjust the BGR values without editing script.
cv2.createTrackbar("c1_b", "Color Trackbars", 0, 255, nothing)
cv2.createTrackbar("c1_g", "Color Trackbars", 0, 255, nothing)
cv2.createTrackbar("c1_r", "Color Trackbars", 0, 255, nothing)
cv2.createTrackbar("c2_b", "Color Trackbars", 0, 255, nothing)
cv2.createTrackbar("c2_g", "Color Trackbars", 0, 255, nothing)
cv2.createTrackbar("c2_r", "Color Trackbars", 0, 255, nothing)
cv2.createTrackbar("c3_b", "Color Trackbars", 0, 255, nothing)
cv2.createTrackbar("c3_g", "Color Trackbars", 0, 255, nothing)
cv2.createTrackbar("c3_r", "Color Trackbars", 0, 255, nothing)
cv2.createTrackbar("c4_b", "Color Trackbars", 0, 255, nothing)
cv2.createTrackbar("c4_g", "Color Trackbars", 0, 255, nothing)
cv2.createTrackbar("c4_r", "Color Trackbars", 0, 255, nothing)
cv2.createTrackbar("c5_b", "Color Trackbars", 0, 255, nothing)
cv2.createTrackbar("c5_g", "Color Trackbars", 0, 255, nothing)
cv2.createTrackbar("c5_r", "Color Trackbars", 0, 255, nothing)
cv2.createTrackbar("c6_b", "Color Trackbars", 0, 255, nothing)
cv2.createTrackbar("c6_g", "Color Trackbars", 0, 255, nothing)
cv2.createTrackbar("c6_r", "Color Trackbars", 0, 255, nothing)

# Read in user input from the trackbars
c1_b = cv2.getTrackbarPos("c1_b", "Color Trackbars")
c1_g = cv2.getTrackbarPos("c1_g", "Color Trackbars")
c1_r = cv2.getTrackbarPos("c1_r", "Color Trackbars")
c2_b = cv2.getTrackbarPos("c2_b", "Color Trackbars")
c2_g = cv2.getTrackbarPos("c2_g", "Color Trackbars")
c2_r = cv2.getTrackbarPos("c2_r", "Color Trackbars")
c3_b = cv2.getTrackbarPos("c3_b", "Color Trackbars")
c3_g = cv2.getTrackbarPos("c3_g", "Color Trackbars")
c3_r = cv2.getTrackbarPos("c3_r", "Color Trackbars")
c4_b = cv2.getTrackbarPos("c4_b", "Color Trackbars")
c4_g = cv2.getTrackbarPos("c4_g", "Color Trackbars")
c4_r = cv2.getTrackbarPos("c4_r", "Color Trackbars")
c5_b = cv2.getTrackbarPos("c5_b", "Color Trackbars")
c5_g = cv2.getTrackbarPos("c5_g", "Color Trackbars")
c5_r = cv2.getTrackbarPos("c5_r", "Color Trackbars")
c6_b = cv2.getTrackbarPos("c6_b", "Color Trackbars")
c6_g = cv2.getTrackbarPos("c6_g", "Color Trackbars")
c6_r = cv2.getTrackbarPos("c6_r", "Color Trackbars")

def getColorTB():
    # Read in user input from the trackbars
    global c1_b, c1_g, c1_r, c2_b, c2_g, c2_r, c3_b, c3_g, c3_r
    global c4_b, c4_g, c4_r, c5_b, c5_g, c5_r, c6_b, c6_g, c6_r
    c1_b = cv2.getTrackbarPos("c1_b", "Color Trackbars")
    c1_g = cv2.getTrackbarPos("c1_g", "Color Trackbars")
    c1_r = cv2.getTrackbarPos("c1_r", "Color Trackbars")
    c2_b = cv2.getTrackbarPos("c2_b", "Color Trackbars")
    c2_g = cv2.getTrackbarPos("c2_g", "Color Trackbars")
    c2_r = cv2.getTrackbarPos("c2_r", "Color Trackbars")
    c3_b = cv2.getTrackbarPos("c3_b", "Color Trackbars")
    c3_g = cv2.getTrackbarPos("c3_g", "Color Trackbars")
    c3_r = cv2.getTrackbarPos("c3_r", "Color Trackbars")
    c4_b = cv2.getTrackbarPos("c4_b", "Color Trackbars")
    c4_g = cv2.getTrackbarPos("c4_g", "Color Trackbars")
    c4_r = cv2.getTrackbarPos("c4_r", "Color Trackbars")
    c5_b = cv2.getTrackbarPos("c5_b", "Color Trackbars")
    c5_g = cv2.getTrackbarPos("c5_g", "Color Trackbars")
    c5_r = cv2.getTrackbarPos("c5_r", "Color Trackbars")
    c6_b = cv2.getTrackbarPos("c6_b", "Color Trackbars")
    c6_g = cv2.getTrackbarPos("c6_g", "Color Trackbars")
    c6_r = cv2.getTrackbarPos("c6_r", "Color Trackbars")

# Get resolution of image
length = np.size(gImg, 0)
width = np.size(gImg, 1)

# Create 6 color images
img_1 = np.zeros((length, width, 3), np.uint8)
img_2 = np.zeros((length, width, 3), np.uint8)
img_3 = np.zeros((length, width, 3), np.uint8)
img_4 = np.zeros((length, width, 3), np.uint8)
img_5 = np.zeros((length, width, 3), np.uint8)
img_6 = np.zeros((length, width, 3), np.uint8)

# Set color images to trackbar colors
img_1 [:] = [c1_b, c1_g, c1_r]
img_2 [:] = [c2_b, c2_g, c2_r]
img_3 [:] = [c3_b, c3_g, c3_r]
img_4 [:] = [c4_b, c4_g, c4_r]
img_5 [:] = [c5_b, c5_g, c5_r]
img_6 [:] = [c6_b, c6_g, c6_r]

def setColor():
    global img_1, img_2, img_3, img_4, img_5, img_6
    img_1 [:] = [c1_b, c1_g, c1_r]
    img_2 [:] = [c2_b, c2_g, c2_r]
    img_3 [:] = [c3_b, c3_g, c3_r]
    img_4 [:] = [c4_b, c4_g, c4_r]
    img_5 [:] = [c5_b, c5_g, c5_r]
    img_6 [:] = [c6_b, c6_g, c6_r]

# Create trackbars for greyscale divisions
cv2.namedWindow("Greyscale Trackbars")
cv2.createTrackbar("g1", "Greyscale Trackbars", 0, 255, nothing)
cv2.createTrackbar("g2", "Greyscale Trackbars", 0, 255, nothing)
cv2.createTrackbar("g3", "Greyscale Trackbars", 0, 255, nothing)
cv2.createTrackbar("g4", "Greyscale Trackbars", 0, 255, nothing)
cv2.createTrackbar("g5", "Greyscale Trackbars", 0, 255, nothing)

# Set greyscale values to default
g1 = 42
g2 = 85
g3 = 128
g4 = 171
g5 = 214

# Define color ranges for color images
lower_1 = [0, 0, 0]
upper_1 = [g1, g1, g1]
lower_2 = [g1+1, g1+1, g1+1]
upper_2 = [g2, g2, g2]
lower_3 = [g2+1, g2+1, g2+1]
upper_3 = [g3, g3, g3]
lower_4 = [g3+1, g3+1, g3+1]
upper_4 = [g4, g4, g4]
lower_5 = [g4+1, g4+1, g4+1]
upper_5 = [g5, g5, g5]
lower_6 = [g5+1, g5+1, g5+1]
upper_6 = [255, 255, 255]

# Define the color ranges as unsigned integers
lower_1 = np.array(lower_1, dtype = "uint8")
upper_1 = np.array(upper_1, dtype = "uint8")
lower_2 = np.array(lower_2, dtype = "uint8")
upper_2 = np.array(upper_2, dtype = "uint8")
lower_3 = np.array(lower_3, dtype = "uint8")
upper_3 = np.array(upper_3, dtype = "uint8")
lower_4 = np.array(lower_4, dtype = "uint8")
upper_4 = np.array(upper_4, dtype = "uint8")
lower_5 = np.array(lower_5, dtype = "uint8")
upper_5 = np.array(upper_5, dtype = "uint8")
lower_6 = np.array(lower_6, dtype = "uint8")
upper_6 = np.array(upper_6, dtype = "uint8")

def setGreyscale():
    global g1, g2, g3, g4, g5
    # Read trackbars to get division values
    g1 = cv2.getTrackbarPos("g1", "Greyscale Trackbars")
    g2 = cv2.getTrackbarPos("g2", "Greyscale Trackbars")
    g3 = cv2.getTrackbarPos("g3", "Greyscale Trackbars")
    g4 = cv2.getTrackbarPos("g4", "Greyscale Trackbars")
    g5 = cv2.getTrackbarPos("g5", "Greyscale Trackbars")

    # Check to make sure the trackbar values are possible
    if g2 <= g1:
        g2 = g1 + 1
    if g3 <= g2:
        g3 = g2 + 1
    if g4 <= g3:
        g4 = g3 + 1
    if g5 <= g4:
        g5 = g4 + 1

    global lower_1, upper_1, lower_2, upper_2
    global lower_3, upper_3, lower_4, upper_4
    global lower_5, upper_5, lower_6, upper_6
    # Define color ranges for color images
    lower_1 = [0, 0, 0]
    upper_1 = [g1, g1, g1]
    lower_2 = [g1+1, g1+1, g1+1]
    upper_2 = [g2, g2, g2]
    lower_3 = [g2+1, g2+1, g2+1]
    upper_3 = [g3, g3, g3]
    lower_4 = [g3+1, g3+1, g3+1]
    upper_4 = [g4, g4, g4]
    lower_5 = [g4+1, g4+1, g4+1]
    upper_5 = [g5, g5, g5]
    lower_6 = [g5+1, g5+1, g5+1]
    upper_6 = [255, 255, 255]

    # Define the color ranges as unsigned integers
    lower_1 = np.array(lower_1, dtype = "uint8")
    upper_1 = np.array(upper_1, dtype = "uint8")
    lower_2 = np.array(lower_2, dtype = "uint8")
    upper_2 = np.array(upper_2, dtype = "uint8")
    lower_3 = np.array(lower_3, dtype = "uint8")
    upper_3 = np.array(upper_3, dtype = "uint8")
    lower_4 = np.array(lower_4, dtype = "uint8")
    upper_4 = np.array(upper_4, dtype = "uint8")
    lower_5 = np.array(lower_5, dtype = "uint8")
    upper_5 = np.array(upper_5, dtype = "uint8")
    lower_6 = np.array(lower_6, dtype = "uint8")
    upper_6 = np.array(upper_6, dtype = "uint8")

# Create masks for the color ranges
mask_1 = cv2.inRange(gCImg, lower_1, upper_1)
mask_2 = cv2.inRange(gCImg, lower_2, upper_2)
mask_3 = cv2.inRange(gCImg, lower_3, upper_3)
mask_4 = cv2.inRange(gCImg, lower_4, upper_4)
mask_5 = cv2.inRange(gCImg, lower_5, upper_5)
mask_6 = cv2.inRange(gCImg, lower_6, upper_6)

def createMasks():
    global mask_1, mask_2, mask_3, mask_4, mask_5, mask_6
    # Create masks for the color ranges
    mask_1 = cv2.inRange(gCImg, lower_1, upper_1)
    mask_2 = cv2.inRange(gCImg, lower_2, upper_2)
    mask_3 = cv2.inRange(gCImg, lower_3, upper_3)
    mask_4 = cv2.inRange(gCImg, lower_4, upper_4)
    mask_5 = cv2.inRange(gCImg, lower_5, upper_5)
    mask_6 = cv2.inRange(gCImg, lower_6, upper_6)

# Apply masks to the papers, creating color parts
filtered_1 = cv2.bitwise_and(img_1, img_1, mask = mask_1)
filtered_2 = cv2.bitwise_and(img_2, img_2, mask = mask_2)
filtered_3 = cv2.bitwise_and(img_3, img_3, mask = mask_3)
filtered_4 = cv2.bitwise_and(img_4, img_4, mask = mask_4)
filtered_5 = cv2.bitwise_and(img_5, img_5, mask = mask_5)
filtered_6 = cv2.bitwise_and(img_6, img_6, mask = mask_6)

# Combine the color parts to generate a complete six-color image
fImg = cv2.bitwise_or(filtered_1, filtered_2, mask = None)
fImg = cv2.bitwise_or(fImg, filtered_3, mask = None)
fImg = cv2.bitwise_or(fImg, filtered_4, mask = None)
fImg = cv2.bitwise_or(fImg, filtered_5, mask = None)
fImg = cv2.bitwise_or(fImg, filtered_6, mask = None)

def applyMasks():
    global filtered_1, filtered_2, filtered_3
    global filtered_4, filtered_5, filtered_6, fImg
    # Apply masks to the papers, creating color parts
    filtered_1 = cv2.bitwise_and(img_1, img_1, mask = mask_1)
    filtered_2 = cv2.bitwise_and(img_2, img_2, mask = mask_2)
    filtered_3 = cv2.bitwise_and(img_3, img_3, mask = mask_3)
    filtered_4 = cv2.bitwise_and(img_4, img_4, mask = mask_4)
    filtered_5 = cv2.bitwise_and(img_5, img_5, mask = mask_5)
    filtered_6 = cv2.bitwise_and(img_6, img_6, mask = mask_6)

    # Combine the color parts to generate a complete six-color image
    fImg = cv2.bitwise_or(filtered_1, filtered_2, mask = None)
    fImg = cv2.bitwise_or(fImg, filtered_3, mask = None)
    fImg = cv2.bitwise_or(fImg, filtered_4, mask = None)
    fImg = cv2.bitwise_or(fImg, filtered_5, mask = None)
    fImg = cv2.bitwise_or(fImg, filtered_6, mask = None)

# Create windows to display the images in them
cv2.namedWindow("Images", cv2.WINDOW_NORMAL)

# Print resolution to shell
print "Width of original image:", width, "\n"
print "Length of original image:", length, "\n"

# Ask for desired resolution of window
desired_width = input("Desired width (side to side) of window? ")
print ""
desired_length = input("Desired length (up and down) of window? ")
print ""

# Resize the "Images" window
cv2.resizeWindow("Images", desired_width, desired_length)

# Display the images in the window using an array
top = np.hstack([gCImg, filtered_1, filtered_2, filtered_3])
bottom = np.hstack([fImg, filtered_4, filtered_5, filtered_6])
combArray = np.vstack([top, bottom])

def stackArray():
    global top, bottom, combArray
    # Display the images in the window using an array
    top = np.hstack([gCImg, filtered_1, filtered_2, filtered_3])
    bottom = np.hstack([fImg, filtered_4, filtered_5, filtered_6])
    combArray = np.vstack([top, bottom])

while True:
    cv2.imshow("Images", combArray)
    k = cv2.waitKey(5)

    if k == 27:
        cv2.destroyAllWindows()
        raise SystemExit()
    elif k == ord("s"):
        cv2.imwrite("greyscale/greyscale_" + imgname, gCImg)
        cv2.imwrite("multifiltered/multifiltered_" + imgname, fImg)
        cv2.destroyAllWindows()
        raise SystemExit()
    else:
        k = cv2.waitKey(1)

    getColorTB()
    setColor()
    setGreyscale()
    createMasks()
    applyMasks()
    stackArray()
