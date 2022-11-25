import sys
import socket
from datetime import datetime as dt


'''
python3 scanner.py

'''

if __name__ == '__main__':

    if len(sys.argv) == 3:
        target = socket.gethostbyname(sys.argv[1])
    else:
        print("invalid amount of arguments")
        print("Syntax python3")
        sys.exit()
    print("*" * 50)
    print("Scanner target" + target)
    print("Scanner target start at " + str(dt.now()))
    print("*" * 50)
    try:
        for port in range(50, 85):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target, port))# return error indicator
            print("Check port {}".format(port))
            if result == 0:
                print("Socket port {} is open".format(port))
            s.close()
    except KeyboardInterrupt:
        print("\n Exiting program")
        sys.exit()
    except socket.gaierror:
        print("Hostname could be resolved")
        sys.exit()
    except socket.error:
        print("could connect is down")
        sys.exit()




