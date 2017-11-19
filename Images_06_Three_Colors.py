'''
    EYW II Unit 3 Exploring Images

    File: Images_06_Three_Colors.py
    Date: 10/31/17
    Author: Alfredo Salazar
    Version: 1.0
    
'''

import cv2
import numpy as np

# Ask for name of image
print ""
imgname = raw_input("Filename of image? ")
folderimgname = "images/" + imgname
print ""

# Read in the image, but in greyscale, to a variable
gImg = cv2.imread(folderimgname, 0)

# Change the greyscale image to a 3 channel image
gCImg = cv2.cvtColor(gImg, cv2.COLOR_GRAY2BGR)

# Get resolution of image
length = np.size(gImg, 0)
width = np.size(gImg, 1)

# Create red, yellow, blue, and green images
redImg = np.zeros((length, width, 3), np.uint8) 
yellowImg = np.zeros((length, width, 3), np.uint8)
blueImg = np.zeros((length, width, 3), np.uint8)

# Set color images to their respective colors
redImg [:] = [0, 0, 255]
yellowImg [:] = [0, 255, 255]
blueImg [:] = [255, 0, 0]

# Create a variable to be able to change the GS ranges
GS_r = input("Greyscale upper limit for red? ")
print ""
GS_y = input("Greyscale upper limit for yellow? ")
print ""

# Define color ranges for red and yellow
lower_r = [0, 0, 0]
upper_r = [GS_r, GS_r, GS_r]
lower_y = [GS_r+1, GS_r+1, GS_r+1]
upper_y = [GS_y, GS_y, GS_y]
lower_b = [GS_y+1, GS_y+1, GS_y+1]
upper_b = [255, 255, 255]

# Define the color ranges as unsigned integers
lower_r = np.array(lower_r, dtype = "uint8")
upper_r = np.array(upper_r, dtype = "uint8")
lower_y = np.array(lower_y, dtype = "uint8")
upper_y = np.array(upper_y, dtype = "uint8")
lower_b = np.array(lower_b, dtype = "uint8")
upper_b = np.array(upper_b, dtype = "uint8")

# Create masks for the color ranges
maskRed = cv2.inRange(gCImg, lower_r, upper_r)
maskYellow = cv2.inRange(gCImg, lower_y, upper_y)
maskBlue = cv2.inRange(gCImg, lower_b, upper_b)

# Apply masks to the papers, creating color parts
filteredRed = cv2.bitwise_and(redImg, redImg, mask = maskRed)
filteredYellow = cv2.bitwise_and(yellowImg, yellowImg, mask = maskYellow)
filteredBlue = cv2.bitwise_and(blueImg, blueImg, mask = maskBlue)

# Combine the color parts to generate a complete four-color image
fImg_part = cv2.bitwise_or(filteredYellow, filteredRed, mask = None)
fImg = cv2.bitwise_or(filteredBlue, fImg_part, mask = None)

# Create windows to display the images in them
cv2.namedWindow("Images", cv2.WINDOW_NORMAL)

# Print resolution to shell
print "Width of orginal image:", width
print ""
print "Length of original image:", length
print ""

# Ask for desired resolution of window
deswidth = input("Desired width (side to side) of window? ")
print ""
deslength = input("Desired length (up and down) of window? ")
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
fi = "filtered/filtered_"
writeNameFi = fi + imgname

# Combine image filename with "greyscale_"
gr = "greyscale/greyscale_"
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
