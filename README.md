# Raspberrypi_connection_to_Server
A guideline on how to code the raspberry pi to talk with an online server.

A good idea to take your project to a next level is to communicate with it online, instead of having the data displayed on a screen, you can check all the data on your phone or computer and interact with your PI from anywhere.

The process is easy, it is a small python code, with a PHP script, and a server to host the communication.

A brief description:
we will start by writing the python code on the pi, let’s say we want to send a distance measured by an Ultrasonic sensor, we will write our normal code to measure the distance, and and then we will use a ‘socket’ to send the data to our server. A socket is one endpoint of a two-way communication link between two programs running on the network. A socket is bound to a port number so that the TCP layer can identify the application that data is destined to be sent to.
The data will be concatenated with an HTTP address linked to the server, where this is the way our PHP script can read the data as an input.
The PHP script will only read the data embedded in the link when called, and it will be stored in a database we previously created.

I hope this was helpful, don’t hesitate to leave any question if you had any problem.
Stay creative and talk to you in the next tutorial.
