import socket
import threading
import sys
import os
import time


def Server_send_file(conn):
    while True:
        try:
            filename = raw_input('input your filename---->')

            if filename == 'exit':
                print('you end the transfer!')
                sys.exit()

            conn.send(filename + '+' + str(os.stat(filename).st_size) + '+')

            time.sleep(0.5)

            fp = open(filename,'rb')
            while True:
                filedata = fp.read(4096)
                if not filedata:
                    break
                conn.send(filedata)

            print "sending over..."
            fp.close()
        except Exception, e:
            print 'no such file,please input valid filename.'
            continue


try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error, msg:
    print 'Failed to create server socket .Error code:' + str(msg[0]) + ',Error message : ' + msg[1]
    sys.exit()
print 'server socket created'

HOST = '192.168.1.109'
PORT = 12346

try:
    s.bind((HOST,PORT))
except socket.error, msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' ,Message ' + msg[1]
    sys.exit()
print 'Socket bind complete ,waiting on:'+ HOST + ':' + str(PORT)

s.listen(10)
print 'server socket now listening'

while True:
    conn ,addr = s.accept()
    print 'Got connection from ',addr[0] + ':' + str(addr[1])
    threading.Thread(target = Server_send_file,args = (conn,)).start()

s.close()
conn.close()
