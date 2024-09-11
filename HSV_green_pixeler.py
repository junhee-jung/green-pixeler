# -*- coding: utf-8 -*-

from multiprocessing import Pool
import glob,os, time
import gc
import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib
import numpy

#change below file location / image type JPG / PNG / JPEG?
os.chdir(r"FILE_LOCATION")
cwd=glob.glob("./*.jpg")
#change file name / location - this will contain all the pixel value
datt=open(r"FILE_LOCATION\no_stem.csv","a")
datt.write("new_run \n")
datt.close()

def green_pixelar(i):
    #change file name / location - this will contain all the pixel value - but same as last time!!!
    datt=open(r"FILE_LOCATION\no_stem.csv","a")
    frame = cv2.imread(i, cv2.IMREAD_COLOR)
    height, width, channels = frame.shape
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #change below find your favourite threashhold and use it
    lower = np.array([0,0 ,0]) #for green roughly 5, 70,70      for yellow roughly 0, 70, 71 
    upper = np.array([255, 255, 255]) #for green roughly 75, 250, 215 for yellow roughly 30, 234, 234)
    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(frame,frame  ,mask=mask)
    countp= cv2.countNonZero(cv2.cvtColor(result, cv2.COLOR_BGR2GRAY))
    plt.figure(1)
    plt.subplot(211)
    plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    plt.subplot(212)
    result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
    plt.imshow(result,  cmap = plt.cm.Spectral)
    #change below adjust DPI if you want the output file to be smaller / make the scipt run much much faster
    #save image location different to original file - it will probably overwrite existing images ...
    plt.savefig(r"FILE_LOCATION2"+"\\"+i.split('\\')[1],dpi=2500)
    datt.write(i.split('\\')[1]+"\t"+str(countp)+"\n")
    datt.close()
    plt.cla() 
    plt.clf()
    plt.ioff()
    plt.close('all')
    gc.collect()
    del result
    del countp
    del mask
    del frame
    del hsv  
    matplotlib.use('Agg')


#this bit contains the code that somehow allows you to run the script as a multi-threaded script change Pool() value to increase / decrease the number of "thread" used  
#(I think technically not using a thread per se but running mulitple of the same script) so even if you have 4 cores you can make pool be 48 it will just run veeeeery slow
if __name__ == '__main__':
    start = time.time()
    #change below to increase / decrease no of cores
    pool = Pool(6)  
    pool.map(green_pixelar, cwd) 
    end = time.time()
    delta = end - start
    print (delta)

