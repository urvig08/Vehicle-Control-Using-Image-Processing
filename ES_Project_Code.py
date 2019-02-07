                                                              
 # **************************************************************************************************************************************************** #
 #  Embedded Systems(ES-5101) Project Code                                                                                                              #
 #                                                                                                                                                      #
 #                                                                                                                                                      #
 #  Project Title: Vehicle Control Using Image Processing                                                                                               #
 #                                                                                                                                                      #
 #  Objective: The main idea of the project is to use Image Processing to control the movement of the Robotic car. Depending on what image is captured, #
 #             the car moves forward, backward, left or right. The Raspberry Pi 2/3 model along with the Raspberry Pi camera module is used to capture  #
 #             the image and store it and then using template matching the correct direction is determined and the movement of the robotic car          #
 #             is controlled.                                                                                                                           #
 #                                                                                                                                                      #                         
 #  Name: Urvi Gada       (801029135) (ugada2uncc.edu)                                                                                                  #
 #        Prachi Kulkarni (801027606) (pkulkar8@unccc.edu)                                                                                              #
 #                                                                                                                                                      #
 #  Components used: Raspberry Pi model 2/3                                                                                                             #
 #                   Raspberry Pi Camera Rev 1.3                                                                                                        #
 #                   Two-wheeled Robotic Car                                                                                                            #                           
 #                   L293D Motor Driver IC                                                                                                              #
 #                   Breadboard                                                                                                                         #
 #                   Jumper Wires                                                                                                                       #
 #                                                                                                                                                      #
 #  Compiled Python IDLE 2                                                                                                                              #
 #                                                                                                                                                      #
 #  Date: 12/12/2017                                                                                                                                    #
 #                                                                                                                                                      #
 #  Specifications: 1. The camera must be able to capture the image correctly.                                                                          #
 #                  2. The motors should be correctly interfaced with the Raspberry Pi board and should move in all directions at the same speed.       #
 #                  3. When the arrow in the image points upwards, the robotic car should move forward.                                                 #
 #                  4. When the arrow in the image points downwards, the robotic car should move forward.                                               #
 #                  5. When the arrow in the image points left, the robotic car should move left.                                                       #
 #   	     	    6. When the arrow in the image points right, the robotic car should move right.                                                     #
 #                                                                                                                                                      #
 # **************************************************************************************************************************************************** #

import cv2
import numpy as np
from picamera import PiCamera
import RPi.GPIO as GPIO
import os
from time import sleep

GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)

#RIGHT MOTOR 
Motor1A = 3
Motor1B = 5

#LEFT MOTOR
Motor2A = 8
Motor2B = 10

TRUE = 1 

#SET THE GPIO PINS TO OUTPUT
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)

GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)


#MOTOR MOVES FORWARD
def process_straight(img_rgb):
    template = cv2.imread("straight1.jpg")
    template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.95
    loc = np.where( res >= threshold)

    count = 0
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
        count = count+1

    print count

    if count > 10:
        cv2.imshow('Detected',img_rgb)
        
        
        print("Straight")
        GPIO.output(Motor1A,GPIO.HIGH)
        GPIO.output(Motor1B,GPIO.LOW)
        GPIO.output(Motor2A,GPIO.HIGH)
        GPIO.output(Motor2B,GPIO.LOW)
        sleep(5)

        print "Stopping motor"
        GPIO.output(Motor1A,GPIO.LOW)
        GPIO.output(Motor1B,GPIO.LOW)
        GPIO.output(Motor2A,GPIO.LOW)
        GPIO.output(Motor2B,GPIO.LOW)
        sleep(5)
        
        cv2.waitKey(1)
        cv2.destroyWindow("Detected")
        #GPIO.cleanup()

    else :
        print("straight not detected")


#MOTOR MOVES BACKWARD
def process_backward(img_rgb):
    template = cv2.imread("down.jpg")
    template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.95
    loc = np.where( res >= threshold)

    count = 0
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
        count = count+1

    print count

    if count > 10:
        cv2.imshow('Detected',img_rgb)
        
        
        print("Backward")
        GPIO.output(Motor1A,GPIO.LOW)
        GPIO.output(Motor1B,GPIO.HIGH)
        GPIO.output(Motor2A,GPIO.LOW)
        GPIO.output(Motor2B,GPIO.HIGH)
        sleep(5)

        print "Stopping motor"
        GPIO.output(Motor1A,GPIO.LOW)
        GPIO.output(Motor1B,GPIO.LOW)
        GPIO.output(Motor2A,GPIO.LOW)
        GPIO.output(Motor2B,GPIO.LOW)
        sleep(5)
        
        cv2.waitKey(1)
        cv2.destroyWindow("Detected")
       # GPIO.cleanup() 

    else :
        print("backward not detected")

		
#MOTOR MOVES RIGHT
def process_right(img_rgb):
    template = cv2.imread("right.jpg")
    template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.95
    loc = np.where( res >= threshold)

    count = 0
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
        count = count+1

    print count

    if count > 10:
        cv2.imshow('Detected',img_rgb)
        
        print("right")
        GPIO.output(Motor1A,GPIO.HIGH)
        GPIO.output(Motor1B,GPIO.LOW)
        GPIO.output(Motor2A,GPIO.LOW)
        GPIO.output(Motor2B,GPIO.LOW)
        sleep(5)

        print "Stopping motor"
        GPIO.output(Motor1A,GPIO.LOW)
        GPIO.output(Motor1B,GPIO.LOW)
        GPIO.output(Motor2A,GPIO.LOW)
        GPIO.output(Motor2B,GPIO.LOW)
        sleep(5)
        cv2.waitKey(3) 
        cv2.destroyWindow("Detected")
     #   GPIO.cleanup()

    else :
        print("right not detected")

		
#MOTOR MOVES LEFT
def process_left(img_rgb):
    template = cv2.imread("left_1.jpg")
    template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.95
    loc = np.where( res >= threshold)

    count = 0
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
        count = count+1

    print count

    if count > 10:
        cv2.imshow('Detected',img_rgb)
        
        
        print("Left")
        GPIO.output(Motor1A,GPIO.LOW)
        GPIO.output(Motor1B,GPIO.LOW)
        GPIO.output(Motor2A,GPIO.HIGH)
        GPIO.output(Motor2B,GPIO.LOW)
        sleep(5)

        print "Stopping motor"
        GPIO.output(Motor1A,GPIO.LOW)
        GPIO.output(Motor1B,GPIO.LOW)
        GPIO.output(Motor2A,GPIO.LOW)
        GPIO.output(Motor2B,GPIO.LOW)
        sleep(5)
        
        cv2.waitKey(2)
        cv2.destroyWindow("Detected")
      #  GPIO.cleanup()

    else :
        print("left not detected")


x = 0
#Camera Initialization
camera = PiCamera()
camera.rotation = 180 

while TRUE:
    #Capture Image    
    camera.start_preview()
    sleep(3)
    camera.capture('/home/pi/ES_project/test.jpg')
    camera.stop_preview()
	
    #Read Image
    img_rgb = cv2.imread("test.jpg")
	
    #Convert Image into gray scale 
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    
	#Check which image is detected
    process_straight(img_rgb)
    process_backward(img_rgb)
    process_right(img_rgb)
    process_left(img_rgb)
    
	#Delete the Image
    os.remove('/home/pi/ES_project/test.jpg')
    print "Image deleted"

