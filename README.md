# Green-pixeler
- Do you want to extract number of "green" pixels from an image? <br/>

- This is a very simple script to extract the number of green pixels from your image (useful if you want to measure your plant size)

- The script is in 2 stages:

1) What is green? using a small script you can play around the sliders and determine which values to mask or to keep. One can use it to also only show yellow pixels in the image or whatever colour ones heart desire within the HSV range <br/>
Please note that **"FILE_LOCATION"** **MUST** be changed - if you  put entire folder location (e.g. C:/Users/junhee-jung/image/* or r"C:\Users\junhee-jung\image\*) **and press q to skip to next image / end the script eventually**
   [HSV_finder.py](https://github.com/junhee-jung/green_pixeler/blob/main/HSV_test.py)
2) Now you know which color range of pixels to keep, apply it to your images. It supports multi-threading, relatively memory efficient, and fast (this is all in comparison to when I first made this script)  <br/>
   [HSV_finder.py]()
