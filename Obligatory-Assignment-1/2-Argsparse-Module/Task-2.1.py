import argparse
import sys

#Method to check the given port
def checkPort(port):
    if 1025 <= port <= 65535: #Checking the given interval
        return True
    else:
        return False

#Method to check the range of given IP address
def checkRangeIP(IP):
    num='' #Setting the num to be a string since we will add the belonging digits and not sum them
    result=True #Setting the result to true by defualt
    for i in IP: #Iterating through the given IP address
        if i.isdigit(): #Selecting out the digits
            num=num+str(i) #Appending the digits
        elif i == '.': #When we come to the end of each block in the IP address
            intNum=int(num) #Parsin the string to an int
            num='' #Emtying the num for later use
            if 0 <= intNum <= 255: #Checking the given interval for each block
                continue #If true, continue
            else:
                result=False #If not true, then update result to be false
                break #And break out
    if num: #If num is not emty, which will be the last block in the IP address
        intNum=int(num) #Parsing the string to int
        if not(0 <= intNum <= 255): #Checking the given interval for each block
            result = False

    return result #Returning the result as a boolean
    
#Method to check if the given IP address is submitted with the right format AKA having 3 dots
def checkDot(IP):
    if IP.count('.') == 3: #Counting the dots to be equeal to 3
        return True
    else:
        return False

def main():
    parser=argparse.ArgumentParser(description="Displaying corresponding port and IP address")

    parser.add_argument('-s', '--server', action='store_true', help='Enable the server mode.')
    parser.add_argument('-c', '--client', action='store_true', help='Enable the client mode.')
    parser.add_argument('-p', '--port', type=int, default=8088, help='Select the port number on which the server will listen.')
    parser.add_argument('-i', '--ip', type=str, default='10.0.0.2', help='Select the IP address where the client should be connected.')

    args=parser.parse_args()

    if args.server:
        if args.port and args.ip and checkPort(args.port) and checkRangeIP(args.ip) and checkDot(args.ip):
            print(f"Output: The server is running with IP address = {args.ip} and port address = {args.port}")
        elif not checkDot(args.ip):
            print(f"Output: Invalid IP. It must be in the format: 10.1.2.3")
        elif not checkRangeIP(args.ip):
            print(f"Output: IP blocks must be within [0, 255]")
        elif not checkPort(args.port):
            print(f"Output: Invalid port. It must be within range [1024, 65535]")
    elif args.client:
        print(f"Output: The client is running with IP address = {args.ip} and port address = {args.port}")
    elif args.server & args.client:
        print('Output: You cannot use both at the same')
    elif len(sys.argv) == 1:
        print('Output: You should run either in server or client mode')
    
main()