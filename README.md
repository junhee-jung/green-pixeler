# Green-pixeler
- Do you want to extract number of "green" pixels from an image? <br/>

- The basic of image masking, as I understand it, is to set the pixels that are below lower limit OR above upper limit as black - 0,0,0 (I think) and countNonZero function is used to count the number of "nonezeros" _i.e._ GREEN or YELLOW pixels

- We converty RGB colour space to HSV (Hue, Saturation, Value) which for some reason works better (it is magical to me, [Wikipedia link](https://en.wikipedia.org/wiki/HSL_and_HSV) )

- This is a very simple script to extract the number of green pixels from your image (useful if you want to measure your plant size)

- The script is in 2 stages:

1) What is green? using a small script you can play around the sliders and determine which values to mask or to keep. One can use it to also only show yellow pixels in the image or whatever colour ones heart desire within the HSV range <br/>
Please note that **"FILE_LOCATION"** **MUST** be changed - if you  put entire folder location (e.g. C:/Users/junhee-jung/image/* or r"C:\Users\junhee-jung\image\*) **and press q to skip to next image / end the script eventually**
   [HSV_finder.py](https://github.com/junhee-jung/green_pixeler/blob/main/HSV_test.py) <br/>
   - Although I do not fully understand how the script work as it is a Frankenstein's monster of codes I borrowed over many online sources, the script takes an image as a "video" and when a mask is applied it plays "video" of newly mask-applied image
3) Now you know which color range of pixels to keep, apply it to your images. It supports multi-threading, relatively memory efficient, and fast (this is all in comparison to when I first made this script)  <br/>
Again please note there are many things that needs to be changed - you are more than welcome to adjust the code however you see fit to minimise the file location / csv name changing. <br/>
common bug? I notice is that sometimes it omit ONE image randomly per run, I don't fully understand why so I would simply recommend running the script twice, Again I am not sure why this is happening. I hope someone with better Python knowledge can help me out here... <br/> 
   [HSV_finder.py](https://github.com/junhee-jung/green-pixeler/blob/main/HSV_green_pixeler.py)

- There are some pip install required dependencies, I am not quite sure which is required Google is probably your best friend for this
