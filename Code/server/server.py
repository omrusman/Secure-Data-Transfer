# //================================================================================================
# // Name        : server.py
# // Author      : Umer 
# // Version     : 
# // Copyright   : Your copyright notice
# // Description : A secure communication channel - Server side 
# //Sources
# //       {1} - https://riptutorial.com/python/example/24255/multi-threaded-tcp-socket-server
# //       {2} - https://www.geeksforgeeks.org/xor-cipher/
# //       {3} - https://cryptography.io/en/latest/fernet/

#These python packages and libraries i am using in this project         
import socket
import threading
# import key_generator as kg
from cryptography.fernet import Fernet
import binascii
import sys

#Constants for communication channel {1}
HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
key = Fernet.generate_key()
print(key)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

#starting the server
def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handling_clients, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() -1}")
        sys.exit()

#client handling and encryption
def handling_clients(conn, addr):
    print(f"[NEW CONNECTION] {ADDR} Connected.")
    print("[STARTING] Server is starting...")

    print("*** WELCOME TO THE FILE TRANSFER SYSTEM ***")
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
                filename = input(str("Please enter the filename: "))
                f = Fernet(key)
                with open(filename, "rb") as file:
                    file_data = file.read(9000000)
                    #Weak encryption XOR cipher {2}
                    data= bytearray(file_data)
                    for index, value in enumerate(data):
                        data[index] = value ^ 20
                    
                    conn.send(data)
                    print("YOUR FILE IS SUCCESSFULLY SENT")

            elif user_input == 2:
                filename = input(str("Please enter the filename: "))
                f = Fernet(key)
                with open(filename, "rb") as file:
                    file_data = file.read(9000000)
                    # Strong encryption aes128 {3}
                    if filename.endswith('.txt'):
                        data= bytearray(file_data)   #for text file
                    elif filename.endswith('.jpg'):
                        data= binascii.hexlify(file_data) #for image file

                encrypted_data = f.encrypt(file_data)
                conn.send(encrypted_data)

                print("YOUR FILE IS SUCCESSFULLY SENT")
            conn.close()
        
        elif user_choice == 2:
            print("*** DO YOU WANT TO USE WEAK OR STRONG ENCRYPTION ***")
            user_input = int(input("CHOOSE OPTION (WEAK=1/STRONG=2): "))
            if user_input == 1:
                filename = input(str("Please enter the filename: "))
                f = Fernet(key)
                with open(filename, "rb") as file:
                    file_data = file.read(9000000)
                    data= bytearray(file_data)
                    for index, value in enumerate(data):
                        data[index] = value ^ 20
                    
                    conn.send(data)
                    print("YOUR FILE IS SUCCESSFULLY SENT")

            elif user_input == 2:
                filename = input(str("Please enter the filename: "))
                f = Fernet(key)
                with open(filename, "rb") as file:
                    file_data = file.read(9000000)
                    if filename.endswith('.txt'):
                        data= bytearray(file_data)   #for text file
                    elif filename.endswith('.jpg'):
                        data= binascii.hexlify(file_data) #for image file

                encrypted_data = f.encrypt(file_data)
                conn.send(encrypted_data)

                print("YOUR FILE IS SUCCESSFULLY SENT")
            conn.close()

        elif user_choice == 3:   
            break

        else:
            print("Please enter a valid input!")
        
print("[STARTING] Server is starting...")
start()    







