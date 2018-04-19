from imutils import contours
from collections import deque
import numpy as np
import argparse
import imutils
import cv2
from Tkinter import Frame, Tk, BOTH, Text, Menu, END
import tkFileDialog
import os.path
import os
import sys

from time import gmtime, strftime


def PT(F):

    Time = strftime("%Y-%m-%d %H%M%S", gmtime())
    
    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-v", "--video", default='Endoscope Test Video.mp4',
    	help="path to the (optional) video file")
    ap.add_argument("-b", "--buffer", type=int, default=10,
    	help="max buffer size")
    ap.add_argument("-f", "--filename",  default='20% 1 CREEP 1min.avi',
    	help="filename to process")
    args = vars(ap.parse_args())
    
    root = Tk()
    root.withdraw()
    #file = tkFileDialog.askopenfilename()
    
    Run = 1
    Setup = 1
    Create = 1
    camera = cv2.VideoCapture(F)
    pts = deque(maxlen=args["buffer"])
    counter = 0
    FirstInitial = 0
    SecondInitial = 0
    FirstPoint = 0
    SecondPoint = 0
    (d1, d2) = (0, 0)
    Difference = 0
    Delta = 0
    PixelToMetric = 0
    DotRadius = 4 #4mm dot diameter
    MeasuredRadius = 0
    RadiusMeasure = 1
    
    TotalPixels = 0
    
    MaxProportion = 0
    MinProportion = 0
    
    hul=0
    huh=179
    sal=0
    sah=255
    val=0
    vah=255
    
    #determine video file name
    
    head, tail = os.path.split(F)
    
    print ("File Selected is: " + tail)
    
    #fourcc = cv2.cv.CV_FOURCC(*'XVID')
    #outCROP = cv2.VideoWriter(F + '_OUTPUT.avi',fourcc, 24.0, (175,150))
    
    if os.path.isfile("SliderVals.txt"):
        f=open("SliderVals.txt",'r')
        hul=int(f.readline())
        huh=int(f.readline())
        sal=int(f.readline())
        sah=int(f.readline())
        val=int(f.readline())
        vah=int(f.readline())
        f.close()
        
        
    def nothing(x):
        pass
    
    while True:
        if os.path.isfile(F):
      
            if (Setup == 1):
          
                #cv2.namedWindow('setupimage')
                #cv2.namedWindow('frame') 
                
                
                if (Create ==1):
                    
                    (grabbed, frame) = camera.read()
                    
                    # Crop Frame to remove side irregularities
                    #Endoscope Resolution = 640x480
                    frame = frame[100:275 , 250:400]
                                  
                    #easy assigments
                    #hh='Hue High'
                    #hl='Hue Low'
                    #sh='Saturation High'
                    #sl='Saturation Low'
                    #vh='Value High'
                    #vl='Value Low'
                    
                    #cv2.createTrackbar(hl, 'setupimage',hul,179,nothing)
                    #cv2.createTrackbar(hh, 'setupimage',huh,179,nothing)
                    #cv2.createTrackbar(sl, 'setupimage',sal,255,nothing)
                    #cv2.createTrackbar(sh, 'setupimage',sah,255,nothing)
                    #cv2.createTrackbar(vl, 'setupimage',val,255,nothing)
                    #cv2.createTrackbar(vh, 'setupimage',vah,255,nothing)
                    
                    Create = 0 
                    
                    #print("Press Esc when trackbars are configured")
                    
                #frame=imutils.resize(frame, width=600)
                hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                
                
                
                #print ("Total Pixels = " + str(TotalPixels))
                
                #read trackbar positions for all
                #hul=cv2.getTrackbarPos(hl, 'setupimage')
                #huh=cv2.getTrackbarPos(hh, 'setupimage')
                #sal=cv2.getTrackbarPos(sl, 'setupimage')
                #sah=cv2.getTrackbarPos(sh, 'setupimage')
                #val=cv2.getTrackbarPos(vl, 'setupimage')
                #vah=cv2.getTrackbarPos(vh, 'setupimage')
                
                #make array for final values
                HSVLOW=np.array([hul,sal,val])
                HSVHIGH=np.array([huh,sah,vah])
            
                #apply the range on a mask
                mask = cv2.inRange(hsv,HSVLOW, HSVHIGH)
                res = cv2.bitwise_and(frame,frame, mask =mask)
                
                #Find Total Number of Pixels in the Cropped Video
                TotalPixels = 123200
                        
                #cv2.imshow('frame', res)
                
                k=cv2.waitKey(10) & 0xFF
                
                Setup = 0
                cv2.destroyWindow('setupimage')
                #f = open("SliderVals.txt", "w")
                #f.write(str(hul) + '\n' )
                #f.write(str(huh) + '\n' )
                #f.write(str(sal) + '\n' )
                #f.write(str(sah) + '\n' )
                #f.write(str(val) + '\n' )
                #f.write(str(vah) + '\n' )
                #f.close()
                pass
        else:
            print('Invalid File Name')
            break
            
        if (Setup == 0):
             
             (grabbed, frame) = camera.read()
             
             
              
             # if no frame,then end of the video
             if args.get("video") and not grabbed:
                 print('No Video')
                 
                 #f = open(tail + ".txt", "a")
                 
                 f = open("Combined.txt", "a")
                 
                 
                 f.write('\n' + '\n' + "Maximum Proportion = " + str(MaxProportion) + '\t' + 
                          "Minimum Proportion = " + str(MinProportion) + '\n')
                 f.close()
                 
                 break
             
             # Crop Frame to remove side irregularities
             #Endoscope Resolution = 640x480         
             frame = frame[100:320 , 40:600]
             
             #frame=imutils.resize(frame, width=600)
             ##blurred = cv2.GaussianBlur(frame, (11, 11), 0)
             hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)     
              
             mask = cv2.inRange(hsv,HSVLOW, HSVHIGH)
             #####mask = cv2.erode(mask, None, iterations=2)
             ######mask = cv2.dilate(mask, None, iterations=2)
    
             WhiteVal = cv2.countNonZero(mask)
             BlackVal = TotalPixels - WhiteVal
             
             ProportionVal = ((float(BlackVal) / float(TotalPixels)) * 100)
             
    
         
             if counter ==1:
                 
                 MaxProportion = ProportionVal       
                 MinProportion = ProportionVal
                 
                 #Create text file with headers
                 
                 #f = open(tail + ".txt", "a")
                 
                 f = open("Combined.txt", "a")
                 
                 f.write(tail + '\n' + Time + '\n' +  "Black Pixel Initial Total" + '\t' + 
                         str(BlackVal) + '\n'+ "Initial Proportion Percentage" + '\t' + 
                         str(ProportionVal) + '\n'+ "Total Pixels = " + str(TotalPixels) + '\n'+
                          "|Frame|" + '\t' + "|BlackPixelVal|" + '\t' + "|Proportion|" + '\n')
                 f.close()
                 
             if counter >=2:  
                 
                 if ProportionVal > MaxProportion:
                     MaxProportion = ProportionVal
                     
                 if ProportionVal < MinProportion:
                     MinProportion = ProportionVal
                     
                 #Open new text file with new timestamp
                 #f = open(tail + ".txt", "a")
                 
                 f = open("Combined.txt", "a")
                 
                 f.write(str(counter) + '\t' + str(BlackVal) + '\t' + str(ProportionVal) + '\n')
                 f.close()
                     
                     
             ##res = cv2.bitwise_and(frame,frame, mask =mask)    
             #outFULL.write(mask)
             #outFULL.release
             
             
             #Find Size of Cropped Frame
             #width, height = frame.shape[:2]
             
             #print "height " + str(height)
             #print "width " + str(width)
             
             #outCROP.write(mask)
             #outCROP.release
             #cv2.imshow('frame', mask)
             counter += 1
             
             k=cv2.waitKey(10)  & 0xFF
             
             if k == 27:             
                 #f = open(tail + ".txt", "a")
                 f = open("Combined.txt", "a")
                 
                 f.write('\n' + '\n' + "Maximum Proportion = " + str(MaxProportion) + '\t' + 
                         + "Minimum Proportion = " + str(MinProportion) + '\n')
                 f.close()             
                 break


for file in os.listdir("."):
    if file.endswith(".avi"):
        PT(file)
    
#root.destroy()         
camera.release()   
out.release
cv2.destroyAllWindows()       