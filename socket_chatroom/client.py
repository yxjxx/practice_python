import socket
import sys  #for exit
import threading

msgIn = ''
msgOut = ''
nickname = ''


def Client_sent_msg(mysocket):
    global nickname,msgOut
    while True:
        msgOut = raw_input('>>')
        msgOut = nickname + ' : ' + msgOut
        mysocket.send(msgOut)

def Client_recv_msg(mysocket):
    global msgIn
    while True:
        try:
            msgIn = mysocket.recv(1024)  #no receive,will stuck,just like raw_input
            #if not msgIn: #msg = nickname + ':' +... ,while always be true,break won't execute .
            #   break
            #if msgOut != msgIn:
            print msgIn
        except:
            break

try:
    #Create an TCP socket
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error,msg:
    print 'Failed to create client socket .Error code:' + str(msg[0]) + ',Error message : ' + msg[1]
    sys.exit()
print "client socket created"

host = '192.168.1.109'
# host = '222.20.59.198'
port = 2500

nickname = raw_input("Please input your nickname: ")

s.connect((host,port))
print 'client socket connected to ' + host
s.send(nickname)

threading.Thread(target = Client_sent_msg,args = (s,)).start()
threading.Thread(target = Client_recv_msg,args = (s,)).start()
