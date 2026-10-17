import socket
import threading
from time import sleep

ip_address = input("Enter IP address: ")
L_port = 10999


def start():
    thread = threading.Thread(target=scan)
    thread.start()

def scan():

    try:
        min_port = int(input('Enter Min Port Number: '))
        max_port = int(input('Enter Max Port Number: '))
    except ValueError:
        print("Enter a valid Number!")
        quit(1)

    if min_port < 1 and max_port < 1:
        print('Port numbers must be between 1 and 65535')
    elif min_port > 65535 and max_port > 65535:
        print('Port numbers must be between 1 and 65535')


    while min_port <= max_port:
        tcp_scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_scanner.settimeout(5)
        try:
            result = tcp_scanner.connect_ex((ip_address, min_port))

            if result == 0:
                print(f"[{min_port}] Port Open")
            else:
                print(f"[{min_port}] Port Closed")
        except Exception as e:
            print(f"[{min_port}]: Error - {e}")

        finally:
            tcp_scanner.close()

        min_port += 1

start()