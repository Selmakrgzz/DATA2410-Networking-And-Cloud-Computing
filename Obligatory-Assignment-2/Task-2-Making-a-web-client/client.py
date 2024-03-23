#import socket module
from socket import *
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description='Http-client')

    #Client input that will indentify the server we want to
    #contact and what object is requested
    parser.add_argument('-i' ,'--serverIP', help='Enter the server IP')
    parser.add_argument('-p' ,'--serverPort', type=int, help='Enter server port')
    parser.add_argument('-f' ,'--filename', help='Enter filename of the requested object')
    args = parser.parse_args()
    serverIP = args.serverIP
    serverPort = args.serverPort
    filename = args.filename

    print(f"Connecting to server at {serverIP}:{serverPort}")

    #Creating a socket called "clientSocket"
    #AF_INET indicates that the underlying network is using IPv4
    #SOCK_STREAM indicates that it is a TCP socket
    clientSocket = socket(AF_INET, SOCK_STREAM)

    #Checking the connection
    try:
        #Connect to the server
        clientSocket.connect((serverIP,serverPort))
        print("Connection established successfully")
    except:
        print("Connection error")
        sys.exit()

    #Sending the HTTP GET request
    request = f'GET /{filename} HTTP/1.1\r\nHost: {serverIP}\r\n\r\n'
    clientSocket.sendall(request.encode())
    #Requesting the server response
    response = clientSocket.recv(1024)
    print(f"Server response: {response.decode()}")

    clientSocket.close()

if __name__ == '__main__':
    main()