#
# Tello Python3 Control Demo 
#
# http://www.ryzerobotics.com/
#
# 1/1/2018

import threading 
import socket
import sys
import time
import platform  

host = ''
port = 9000
locaddr = (host,port) 


# UDP socket 만들기
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

tello_address = ('192.168.10.1', 8889)

sock.bind(locaddr)

def recv():
    count = 0
    while True: 
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print ('\nExit . . .\n')
            break


print ('\r\n\r\nTello Python3 Demo.\r\n')

print ('Tello: command takeoff land flip forward back left right \r\n       up down cw ccw speed speed?\r\n')

print ('end -- quit demo.\r\n')


#recvThread 만들기
recvThread = threading.Thread(target=recv)
recvThread.start()

while True: 
    try:
        python_version = str(platform.python_version())
        version_init_num = int(python_version.partition('.')[0]) 
       # 파이썬 버전 체크
        if version_init_num == 3: # 파이선 버전이 3이면 input함수로 보냄
            msg = input("");
        elif version_init_num == 2: # 파이선 버전이 2이면 raw_input함수로 보냄
            msg = raw_input("");
        
        if not msg:
            break  

        if 'end' in msg:
            print ('...')
            sock.close()  
            break

        # 데이터 보내는 부분
        msg = msg.encode(encoding="utf-8") 
        sent = sock.sendto(msg, tello_address)
        
    except KeyboardInterrupt:
        print ('\n . . .\n')
        sock.close()  
        break




