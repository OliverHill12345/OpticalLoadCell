# OpticalLoadCell
Image Processing Python Script for the use with an Optical Load Cell System

This Python script was generated in conjunction with AnacondaPython to install the majority of libraries utilised

The latest release of OpenCV 2.4 library was installed seperately, with the cv2.pyd file moved from the downloaded OpenCV folder to Anaconda\Lib\site-package directory

To enable correct functionality, a new Environmental Variable had to be created on the Windows 7 Operating system used.
The variable made was called "OPENCV DIR" with the value being the directory of the vc14 folder located within the OpenCV Folder

The SETUP.py file found in this repository is for use with a single video file, allowing for the proper masking of the load cell image through the use of trackbars. This file saves the trackbar values to a text file called "SliderVals.txt" which is then used by the "BATCH.py" file for use on multiple .avi files located in the same directory as the "BATCH.py" file.

The "CAMERA_VIEW.py" file allows for the load cell camera image to be viewed in realtime, with the video saved to a file.
