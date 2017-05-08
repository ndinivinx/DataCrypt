#!/usr/bin/python

import sys      		#for Ceasar cipher
from Crypto.Cipher import AES	#for AES (Downloaded PyCrypto)

print("*********************************************THIS IS DATACRYPT*********************************************")
print("*********************************************C73@T0R ---> V!NX*********************************************")
print("*********************************************git--> @ndinivinx*********************************************")

print('Enter your text here: \n')
msg = input()				#this is the message to be encrypted later

print("Choose any 1 of these 3 choices\n" + "Choose 1 for AES encryption\n" + "Choose 2 for Caesar Cipher\n" + "Choose 3 to exit\n\n") #menu
print("Please make your choice now: ")
choice = input()			#selection of menu item

if choice == "1":	#if choice is for AES do the below
	print("Enter a secret key ONLY known by the receiver\n")
	key = input()			#enter secret key
	v = AES.new(key, AES.MODE_CBC, 'This is my IV000')
#object v is instantiated. v is key_length, CBC is the mode an the last stringis the initialization vector
	ciphertxt = v.encrypt(msg)	#encrypted message is stored in ciphertxt but as bytes
	ciphertext = str(ciphertxt,'utf-16')	#this converts bytes to a string in unicode
	print("Your ciphetrtext is: "+ciphertext)	#this line prints the ciphertext
	
elif choice == "2":	#choice for Ceaser cipher
	def encrypt(msg):
		ciphertxt = ''
		k = int (input("Enter your chosen transposition number: ")) #number of transpositions
	
		for each in msg:
			c = (ord(each)+k) % 126	#iterates each letter and transposes it
		
			if c < 32:  #if c is less 32, add 31 to move to the tranposed value (capital)
				c+=31
			
			ciphertxt += chr(c) #creates a concatenated stream of characters
		
		print ('Your encrypted message is: ' + ciphertxt)
	encrypt(msg) #calls the  function for encryption

elif choice == "3":		#this choice exits the program
	print("Goodbye. See you again soon!!")
	exit()
else:
	print("I don't understand your choice.") #this is used when the chosen option is invalid
