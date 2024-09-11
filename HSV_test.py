# -*- coding: utf-8 -*-
import cv2, glob,os
import numpy as np

def nothing(x):
    pass
#CHANGE BELOW
print("hello, to quit press Q on keyboard - if sliders does not work press q and start again")
print( "did you change FILE_LOCATION? e.g. C:/Users/photo/*")
img_l=glob.glob( FILE_LOCATION )
#CHANGE above
for img in img_l:
    image = cv2.imread(img)
    scale_percent = 50
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 200)
    dim = (width, height)
    image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    cv2.namedWindow('image')
    cv2.createTrackbar('HMin', 'image', 0, 179, nothing)
    cv2.createTrackbar('SMin', 'image', 0, 255, nothing)
    cv2.createTrackbar('VMin', 'image', 0, 255, nothing)
    cv2.createTrackbar('HMax', 'image', 0, 179, nothing)
    cv2.createTrackbar('SMax', 'image', 0, 255, nothing)
    cv2.createTrackbar('VMax', 'image', 0, 255, nothing)
    cv2.setTrackbarPos('HMax', 'image', 179)
    cv2.setTrackbarPos('SMax', 'image', 255)
    cv2.setTrackbarPos('VMax', 'image', 255) 
    while(1):
        # Get current positions of all trackbars
        hMin = cv2.getTrackbarPos('HMin', 'image')
        sMin = cv2.getTrackbarPos('SMin', 'image')
        vMin = cv2.getTrackbarPos('VMin', 'image')
        hMax = cv2.getTrackbarPos('HMax', 'image')
        sMax = cv2.getTrackbarPos('SMax', 'image')
        vMax = cv2.getTrackbarPos('VMax', 'image')
        # Set minimum and maximum HSV values to display
        lower = np.array([hMin, sMin, vMin])
        upper = np.array([hMax, sMax, vMax])
        a=(hMin,sMin,vMin,hMax,sMax,vMax)
        # Convert to HSV format and color threshold
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower, upper)
        result = cv2.bitwise_and(image, image, mask=mask)
        countp= cv2.countNonZero(cv2.cvtColor(result, cv2.COLOR_BGR2GRAY))
        print (countp)
        kernel = np.ones((2,2),np.uint8)
        erosion = cv2.erode(result,kernel,iterations = 1)
        # Print if there is a change in HSV value
        # Display result image
        erosion=cv2.resize(erosion,None,fx=0.5,fy=0.5)
        result=cv2.resize(result,None,fx=0.2,fy=0.2)
        cv2.imshow(img.split("\\")[-1], result)   
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
    print (a)
