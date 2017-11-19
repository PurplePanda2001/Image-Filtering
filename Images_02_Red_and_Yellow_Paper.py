'''
    EYW II Unit 3 Exploring Images

    File: Images_02_Red_and_Yellow_Paper.py
    Date: 10/24/17
    Author: Alfredo Salazar
    Version: 1.0
    
'''

import cv2
import numpy as np

# Ask for name of image
print ""
imgname = raw_input("Filename of image? ")
print ""

# Read in the image, but in greyscale, to a variable
gImg = cv2.imread(imgname, 0)

# Get resolution of image
length = np.size(gImg, 0)
width = np.size(gImg, 1)

# Create red image and yellow image
redImg = np.zeros((length, width, 3), np.uint8) 
yellowImg = np.zeros((length, width, 3), np.uint8)

# Set red and yellow image to their respective colors
redImg [:] = [0, 0, 255]
yellowImg [:] = [0, 255, 255]

# Test out red and yellow images
print "Color value of redImg at 50, 50: ", redImg[50, 50]
print "Color value of yellowImg at 50, 50: ", yellowImg[50, 50]

# Change the greyscale image to a 3 channel image
gCImg = cv2.cvtColor(gImg, cv2.COLOR_GRAY2BGR)

# Test out BGR value of greyscale converted image
print ""
print "Color value of gCImg at 50, 50: ", gCImg[50, 50]
print "Color value of gCImg at 12, 76: ", gCImg[12, 76]
print "Color value of gCImg at 137, 15: ", gCImg[137, 15]

# Define color ranges for red and yellow
lower_r = [0, 0, 0]
upper_r = [127, 127, 127]
lower_y = [128, 128, 128]
upper_y = [255, 255, 255]

# Define the color ranges as unsigned integers
lower_r = np.array(lower_r, dtype = "uint8")
upper_r = np.array(upper_r, dtype = "uint8")
lower_y = np.array(lower_y, dtype = "uint8")
upper_y = np.array(upper_y, dtype = "uint8")

# Create masks for the red and yellow ranges
maskRed = cv2.inRange(gCImg, lower_r, upper_r)
maskYellow = cv2.inRange(gCImg, lower_y, upper_y)

# Apply masks to the papers, creating red and yellow parts
filteredRed = cv2.bitwise_and(redImg, redImg, mask = maskRed)
filteredYellow = cv2.bitwise_and(yellowImg, yellowImg, mask = maskYellow)

# Combine the red and yellow parts to generate a complete two-color image
fImg = cv2.bitwise_or(filteredYellow, filteredRed, mask = None)

# Create windows to display the images in them
cv2.namedWindow("Images", cv2.WINDOW_NORMAL)

# Ask for desired resolution of window
print ""
deswidth = input("Desired width (side to side) of window? ")
print ""
deslength = input("Desired length (up and down) of window? ")
print ""

# Print resolution to shell
print "Width of orginal image:", width
print ""
print "Length of original image:", length
print ""

# Resize the "Images" window
cv2.resizeWindow("Images", deswidth, deslength)

# Display the images in the window using an array
top = np.hstack([gCImg, fImg])
bottom = np.hstack([filteredRed, filteredYellow])
combArray = np.vstack([top, bottom])

cv2.imshow("Images", combArray)

# Assign waitkey function to variable k
k = cv2.waitKey(0)

# Combine image filename with "filtered_"
fi = "filtered_"
writeNameFi = fi + imgname

# Combine image filename with "greyscale_"
gr = "greyscale_"
writeNameGr = gr + imgname

# Destroys windows and quits or saves image and quits
while True:
    if (k == 27):
        cv2.destroyAllWindows()
        raise SystemExit()
    elif (k == ord("s")):
        cv2.imwrite(writeNameGr, gCImg)
        cv2.imwrite(writeNameFi, fImg)
        cv2.destroyAllWindows()
        raise SystemExit()
    else:
        k = cv2.waitKey(0)
        
