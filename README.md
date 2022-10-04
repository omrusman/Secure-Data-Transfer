# Secure-Data-Transfer
An Application to transfer data securely. 

# Importance of the Project
I have created this project that allow users to send data files using a secure communication channel. I have implemented two types of encryption techniques on the communication channel. A weak and a strong encryption. For the weak encryption i am converting the file data into bytes. After converting into bytes then I am using a very basic encryption
technique in which I am using the enumerate function which basically changes the bytes collection into an enumerate object. It gives two outputs (key and value). Then I am using XOR operator for encrypting my byte data. For strong encryption i am using
the FERNET encryption technique which uses 128-bit AES encryption.
With this application you can transfer files securely over the internet. For transferring data both sender and receiver needs to run the application.

# How to run the project
I have created the bash files for both the server and client. They are in the "Application" folder. 
1. Run both files on same PC or remotely and follow the instructions.
2. The server will show you the IP address and the secret key. 
3. You need to copy this secret key and send to the client. 
4. You need to select which encryption and file (add the file extention "text.txt") you want to transfer on the client side first.
5. Select the encryption type.
6. On server side select send file and on the client side select receive file option.
7. Enter the name of the file that you want to receive on the client side first (make sure the file is already inside the server folder).
8. Enter the name of the file that you want to send on the server side. 
9. Done. 

(Because of the already provided IP address on the client side maybe the bash file will not work properly. In this case please run the program using the method mentioned below).

# Running from the python script. 
1. Run the server.py script file on the terminal.
2. It will show you the secret key and the IP address.
3. Open the client.py script and check if the IP address is same, if it is not same then please write the correct IP address. 
4. Run the client.py script file on the terminal. 
5. Enter the secret key on the client side. 
6. You need to select which encryption and file (add the file extention "text.txt") you want to transfer on the client side first.
7. On server side select send file and on the client side select receive file option.
8. Enter the name of the file that you want to receive on the client side first (make sure the file is already inside the server folder).
9. Enter the name of the file that you want to send on the server side. 
10. Done. 

Here is an explained [manual](https://drive.google.com/file/d/1Lg6KITdR647MYKSxUZ_a9dqdlqTe18FZ/view?usp=sharing) how i created this application.
