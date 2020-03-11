# Started from Tello Template
# This Python app is in the Public domain
# Some parts from Tello3.py

import threading, socket, sys, time, subprocess


# GLOBAL VARIABLES DECLARED HERE....

def cube():
   sendmsg('up 100')
   sendmsg('forward   150')
   sendmsg('cw 90')
   sendmsg('forward 150')
   sendmsg('cw 90')
   sendmsg('forward 150')
   sendmsg('cw 90')
   sendmsg('forward 150')
   sendmsg('down 50')
   for i in range(4):
        sendmsg('cw 90')
        sendmsg('forward 150')
        sendmsg('up 50')
        sendmsg('down 50')
    sendmsg('cw 135')
    sendmsg('forward 75')
    sendmsg('ccw 45')
    sendmsg('up 60')
    sendmsg('flip b')
    sendmsg('flip f')


host = ''
port = 9000
locaddr = (host,port)
tello_address = ('192.168.10.1', 8889) # Get the Tello drone's address



# Creates a UDP socketd
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(locaddr)


def recv():
    count = 0
    while True:
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print ('\n****Keep Eye on Drone****\n')
            break


def sendmsg(msg, sleep = 6):
    print("Sending: " + msg)
    msg = msg.encode(encoding="utf-8")
    sock.sendto(msg, tello_address)
    time.sleep(sleep)

# recvThread create
recvThread = threading.Thread(target=recv)
recvThread.start()


# CREATE FUNCTIONS HERE....


print("\nMiles And Carson")
print("Program Name: Cube ")
print("Date: 3/11/20 ")
print("\n****CHECK YOUR TELLO WIFI ADDRESS****")
print("\n****CHECK SURROUNDING AREA BEFORE FLIGHT****")
ready = input('\nAre you ready to take flight: ')


try:
    if ready.lower() == 'yes':
        print("\nStarting Drone!\n")

        sendmsg('command', 0)
        sendmsg('takeoff')


        cube()

        sendmsg('land')

        print('\nGreat Flight!!!')

    else:
        print('\nMake sure you check WIFI, surroundings, co-pilot is ready, re-run program\n')
except KeyboardInterrupt:
    sendmsg('emergency')

breakr = True
sock.close()
