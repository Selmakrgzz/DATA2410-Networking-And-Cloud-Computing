import argparse
import sys

def checkPort(port):
    if 1025 <= port <= 65535:
        return True
    else:
        return False

def checkRangeIP(IP):
    num=''
    result=True
    for i in IP:
        if i.isdigit():
            num=num+str(i)
        elif i == '.':
            intNum=int(num)
            num=''
            if 0 <= intNum <= 255:
                continue
            else:
                result=False
                break
    if num:
        intNum=int(num)
        if not(0 <= intNum <= 255):
            result = False

    return result
    

def checkDot(IP):
    if IP.count('.') == 3:
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