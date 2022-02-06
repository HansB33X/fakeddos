import time
import os
import pyfiglet

try:
	print(pyfiglet.figlet_format("DDoS"))
	print("by HansB33X\n")

	ip_input = input("Masukan IP Target : ")
	while True:
		print("DDoS Ke IP Target", ip_input)
except:
	print("command yang anda masukan salah...")
