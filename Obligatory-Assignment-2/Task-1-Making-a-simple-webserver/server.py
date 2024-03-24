#import socket module
from socket import *
import sys # In order to terminate the program

def main():
    #Create a socket called serverSocket
    serverSocket = socket(AF_INET, SOCK_STREAM)
    #Prepare a sever socket
    server_port = 8000
    server_ip = '127.0.0.1'
    
    try:
        #Establishes a connection between the server's IP address and the specified port number
        serverSocket.bind((server_ip, server_port))
        #Waiting for a connection
        serverSocket.listen(1)
        print('The server is ready to receive')

        while True:
            #Establish the connection print('Ready to serve...') connectionSocket, addr =
            connectionSocket, addr = serverSocket.accept()
            print(f"Connection established from {addr}")

            try:
                #Receiving the message from url client side
                message = connectionSocket.recv(1024).decode()

                #Extracting the filename
                filename = message.split()[1]

                #Opening the file
                f = open(filename[1:])

                #Reading the file to be sent back to client
                outputdata = f.read()
                print(filename)

                #Send one HTTP header line into socket
                http_response = "HTTP/1.1 200 OK\r\n\r\n"

                #Send the content of the requested file to the client
                for i in range(0, len(outputdata)):
                    connectionSocket.send(outputdata[i].encode())
                connectionSocket.send("\r\n".encode())
                
            except IOError:
                #Send response message for file not found
                http_response = "HTTP/1.1 404 Not Found\r\n\r\n"
            
            #Sending the http repsonse to client side
            connectionSocket.send(http_response.encode())

            # Close client socket
            connectionSocket.close()

    except Exception as e:
        print('Server error: ', e )
             
    finally:
        serverSocket.close()
        sys.exit()#Terminate the program after sending the corresponding data

if __name__ == '__main__':
    main()