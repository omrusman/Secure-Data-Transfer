# //================================================================================================
# // Name        : client.py
# // Author      : Umer 
# // Version     : 
# // Copyright   : Your copyright notice
# // Description : A secure communication channel - client side 
# //Sources
# //       {1} - https://riptutorial.com/python/example/24255/multi-threaded-tcp-socket-server
# //       {2} - https://www.geeksforgeeks.org/xor-cipher/
# //       {3} - https://cryptography.io/en/latest/fernet/

#These python packages and libraries i am using in this project
from multiprocessing.reduction import send_handle
import socket
# import key_generator as kg
from cryptography.fernet import Fernet
import binascii

#Constants for communication channel {1}
HEADER = 64
PORT = 5050
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.56.1"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

print("*** WELCOME TO THE FILE TRANSFER SYSTEM ***")
key = input("ENTER THE SECRET KEY: ")
#Decryption
while True:
    print("CHOOSE OPTION")
    print("1. Receive File: ")
    print("2. Send File: ")
    print("3. Exit: ")
    user_choice = int(input("\nEnter your Choice: "))

    if user_choice == 1:
    	print("*** DO YOU WANT TO USE WEAK OR STRONG ENCRYPTION ***")
    	user_input = int(input("CHOOSE OPTION (WEAK=1/STRONG=2): "))
    	if user_input == 1:
    		filename = input(str("Please enter filename you want to Receive: "))
    		encrypted_file = f"encrypted - {filename}"
    		file = open(filename, "wb")
    		file_enc = open(encrypted_file, "wb")
    		file_data = client.recv(9000000)
    		data= bytearray(file_data)
            #Weak encryption XOR cipher {2}
    		for index, value in enumerate(data):
    			data[index] = value ^ 20
    		file_enc.write(file_data)
    		file.write(data)
    		file.close()
    		print("File has been received successfully.")
    	elif user_input == 2:
    		filename = input(str("Please enter filename you want to Receive: "))
    		encrypted_file = f"encrypted - {filename}"
    		file = open(filename, "wb")
    		file_enc = open(encrypted_file, "wb")
    		file_data = client.recv(9000000)
            # Strong encryption aes128 {3}
    		if filename.endswith('.txt'):
    			data= bytearray(file_data) #for text file
    			file_enc.write(data)
    			f = Fernet(key)
    			decrypted_data = f.decrypt(file_data)
    			file.write(decrypted_data)
    			file_enc.close()
    			file.close()
    		elif filename.endswith('.jpg'):
    			data= binascii.hexlify(file_data) #for image file
    			file_enc.write(data)
    			f = Fernet(key)
    			decrypted_data = f.decrypt(file_data)
    			file.write(decrypted_data)
    			file_enc.close()
    			file.close()
    			print("YOUR FILE IS SUCCESSFULLY RECEIVED!")

    elif user_choice == 2:
    	print("*** DO YOU WANT TO USE WEAK OR STRONG ENCRYPTION ***")
    	user_input = int(input("CHOOSE OPTION (WEAK=1/STRONG=2): "))
    	if user_input == 1:
    		filename = input(str("Please enter filename you want to Receive: "))
    		encrypted_file = f"encrypted - {filename}"
    		file = open(filename, "wb")
    		file_enc = open(encrypted_file, "wb")
    		file_data = client.recv(9000000)
    		data= bytearray(file_data)
    		for index, value in enumerate(data):
    			data[index] = value ^ 20
    		file_enc.write(file_data)
    		file.write(data)
    		file.close()
    		print("File has been received successfully.")
    	elif user_input == 2:
    		filename = input(str("Please enter filename you want to Receive: "))
    		encrypted_file = f"encrypted - {filename}"
    		file = open(filename, "wb")
    		file_enc = open(encrypted_file, "wb")
    		file_data = client.recv(9000000)
    		if filename.endswith('.txt'):
    			data= bytearray(file_data) #for text file
    			file_enc.write(data)
    			f = Fernet(key)
    			decrypted_data = f.decrypt(file_data)
    			file.write(decrypted_data)
    			file_enc.close()
    			file.close()
    		elif filename.endswith('.jpg'):
    			data= binascii.hexlify(file_data) #for image file
    			file_enc.write(data)
    			f = Fernet(key)
    			decrypted_data = f.decrypt(file_data)
    			file.write(decrypted_data)
    			file_enc.close()
    			file.close()

    		print("YOUR FILE IS SUCCESSFULLY RECEIVED!")

    elif user_choice == 3:
    	break

    else:
    	print("Please enter a valid input!")
