#!/usr/bin/env python

import time
import RPi.GPIO as GPIO
import cgi
import cgitb


def setservo(range):
	if -90.0<=range<=90.0:
		duty=2.5+(range+90)*(12.0-2.5)/180
		servo.ChangeDutyCycle(duty)
		
		
print('Content-type: text/html; charset=UTF-8\r\n')
print('Web Servo')

print('<form action="" method="post">')
print('<p>')
print('äpìxÅF')
print('input type="number" name="angle"')
print('</p>')
print('<input type="submit" value="ëóêM">')
print('</form>')


GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)

form = cgi.FieldStorage()
angle = form.getvalue("angle")

servo = GPIO.PWM(2, 50)
servo.start(angle)


