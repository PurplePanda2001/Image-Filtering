'''
    EYW II Unit 3 Exploring Images

    File: Images_01_Color_to_GS.py
    Date: 10/21/17
    Author: Alfredo Salazar
    Version: 1.0

'''
# Import the libraries to use
import cv2
import numpy as np

# Ask for name of image
print ""
imgname = raw_input("Filename of image? ")
print ""

# Read in the image to a variable
cImg = cv2.imread(imgname)
# Read in the image, but in greyscale, to a variable
gImg = cv2.imread(imgname, 0)

# Get resolution of orginal image
length = np.size(cImg, 0)
width = np.size(cImg, 1)

# Create red image and yellow image
redImg = np.zeros((length, width, 3), np.uint8) 
yellowImg = np.zeros((length, width, 3), np.uint8)

# Set red and yellow image to their respective colors
redImg [:] = [0, 0, 255]
yellowImg [:] = [0, 255, 255]

# Create windows for images to be in
cv2.namedWindow("Color Image", cv2.WINDOW_NORMAL)
cv2.namedWindow("GS Image", cv2.WINDOW_NORMAL)

# Resize the created windows
cv2.resizeWindow("Color Image", 640, 480)
cv2.resizeWindow("GS Image", 640, 480)

# Displays images in the created windows
cv2.imshow("Color Image", cImg)
cv2.imshow("GS Image", gImg)

# Assign waitkey function to variable k
k = cv2.waitKey(0)

# Destroys windows and quits or saves image and quits
while True:
    if (k == 27):
        cv2.destroyAllWindows()
        raise SystemExit()
    elif (k == ord("s")):
        cv2.imwrite(writeName, gImg)
        cv2.destroyAllWindows()
        raise SystemExit()
    else:
        k = cv2.waitKey(0)
