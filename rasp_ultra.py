import RPi.GPIO as GPIO
import socket //importing socket library
import time
import math
GPIO.setmode(GPIO.BCM)

host = "alawiya51.mypressonline.com" //hostname goes here
port = 80 // setting the port number

//setting the ultrasonic sensor pins
TRIG = 23 
ECHO = 24

print "Distance Measuremnet In Progress"

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, False)
print "Waiting for Sensor to Settle"

//Create a method to send the data
def sendData():
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) //initiating a socket
		s.connect((host , port)) // connecting to the server
		time.sleep(2)
		GPIO.output(TRIG, True)
		time.sleep(0.00001)
		GPIO.output(TRIG, False)
		while GPIO.input(ECHO)==0:
			pulse_start = time.time()
		while GPIO.input(ECHO)==1:
			pulse_end = time.time()
		pulse_duration = pulse_end - pulse_start //measuring the time between both pulses
		distance = pulse_duration * 171.50
		distance = round(distance,2) //calculating the distance
		request = "GET /insert.php?x=" + str(distance) + \
				  " HTTP/1.1\r\nHost: " + host + "\r\n\r\n" //writing the request
		s.send(request) //sending the request to the server
		request = ""
		print "Distance : ",distance, "m\n"
		

while True:
	sendData();
	time.sleep(60) //send the data to the server every minute
done;
GPIO.cleanup()