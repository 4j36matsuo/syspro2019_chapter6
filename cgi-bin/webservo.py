#!/usr/bin/env python

import cgi
import cgitb    #display CGI error on browser
import time
import RPi.GPIO as GPIO


print('Content-type: text/html; charset=UTF-8\r\n')
print('Web Servo')

print('<form action="" method="post">')
print('<p>')
print('Angle:')
print('<input type="number" name="angle" value="0">')
print('</p>')
print('<input type="submit" name="set" value="set">')
print('</form>')


def setservo(range):
	if -90<=range<=90:
		duty=2.5+(range+90)*(12.0-2.5)/180
		servo.ChangeDutyCycle(duty)

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
servo = GPIO.PWM(2, 50)
servo.start(0.0)

form = cgi.FieldStorage()
angle = form.getvalue("angle")

setservo(int(angle))

print('Motor set to '+angle)


