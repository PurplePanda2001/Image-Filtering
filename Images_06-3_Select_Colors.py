'''
    EYW II Unit 3 Exploring Images

    File: Images_06-3_Select_Colors.py
    Date: 10/31/17
    Author: Alfredo Salazar
    Version: 1.0
    
'''

import cv2
import numpy as np

import os
print "\nAvailable image filenames: "
path = "images"
dirs = os.listdir(path)
for file in dirs:
    print file

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

# Create 6 color images
img_1 = np.zeros((length, width, 3), np.uint8) 
img_2 = np.zeros((length, width, 3), np.uint8)
img_3 = np.zeros((length, width, 3), np.uint8)
img_4 = np.zeros((length, width, 3), np.uint8)

# Define colors
red = [0, 0, 255]
yellow = [0, 255, 255]
green = [0, 255, 0]
blue = [255, 0, 0]

colors = ["red", "yellow", "green", "blue"]

# Print available colors
print "Available colors:"
for i in colors:
    print i
print ""

# Ask for colors and set color images to them
img_1 [:] = input("Select color 1: ")
img_2 [:] = input("Select color 2: ")
img_3 [:] = input("Select color 3: ")
img_4 [:] = input("Select color 4: ")
print ""

# Ask for greyscale threshold
GS = input("Greyscale threshold? ")
print ""

# Define color ranges for color images
lower_1 = [0, 0, 0]
upper_1 = [GS, GS, GS]
lower_2 = [GS+1, GS+1, GS+1]
upper_2 = [(GS*2)+1, (GS*2)+1, (GS*2)+1]
lower_3 = [(GS*2)+2, (GS*2)+2, (GS*2)+2]
upper_3 = [(GS*3)+2, (GS*3)+2, (GS*3)+2]
lower_4 = [(GS*3)+3, (GS*3)+3, (GS*3)+3]
upper_4 = [255, 255, 255]

# Define the color ranges as unsigned integers
lower_1 = np.array(lower_1, dtype = "uint8")
upper_1 = np.array(upper_1, dtype = "uint8")
lower_2 = np.array(lower_2, dtype = "uint8")
upper_2 = np.array(upper_2, dtype = "uint8")
lower_3 = np.array(lower_3, dtype = "uint8")
upper_3 = np.array(upper_3, dtype = "uint8")
lower_4 = np.array(lower_4, dtype = "uint8")
upper_4 = np.array(upper_4, dtype = "uint8")

# Create masks for the color ranges
mask_1 = cv2.inRange(gCImg, lower_1, upper_1)
mask_2 = cv2.inRange(gCImg, lower_2, upper_2)
mask_3 = cv2.inRange(gCImg, lower_3, upper_3)
mask_4 = cv2.inRange(gCImg, lower_4, upper_4)

# Apply masks to the papers, creating color parts
filtered_1 = cv2.bitwise_and(img_1, img_1, mask = mask_1)
filtered_2 = cv2.bitwise_and(img_2, img_2, mask = mask_2)
filtered_3 = cv2.bitwise_and(img_3, img_3, mask = mask_3)
filtered_4 = cv2.bitwise_and(img_4, img_4, mask = mask_4)

# Combine the color parts to generate a complete six-color image
fImg_part1 = cv2.bitwise_or(filtered_1, filtered_2, mask = None)
fImg_part2 = cv2.bitwise_or(filtered_3, filtered_4, mask = None)

fImg = cv2.bitwise_or(fImg_part1, fImg_part2, mask = None)

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
top = np.hstack([gCImg, filtered_1, filtered_2])
bottom = np.hstack([fImg, filtered_3, filtered_4])
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
