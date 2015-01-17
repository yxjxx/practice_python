import socket
import sys  #for exit
import threading

cond = threading.Condition()

try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error, msg:
    print 'Failed to create server socket .Error code:' + str(msg[0]) + ',Error message : ' + msg[1]
    sys.exit()
print 'server socket created'

#host = socket.gethostname()
HOST = '192.168.1.109'
# HOST = '222.20.59.198'
PORT = 2500
data = ''

try:
    s.bind((HOST,PORT))
except socket.error, msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' ,Message ' + msg[1]
    sys.exit()
print 'Socket bind complete ,waiting on :'+ HOST + ':' + str(PORT)

s.listen(10)
print 'server socket now listening'

def NotifyAll(public_msg):
    global data
    if cond.acquire():
        data = public_msg
        cond.notifyAll()
        cond.release()

def Server_recv_msg(conn,nickname):
    global data
    while True:
        try:
            temp = conn.recv(1024)
            if not temp:
                conn.close()
                return
            NotifyAll(temp)  #awake ClientThreadOut thread
            print data
        except:
            NotifyAll(nickname + " leave the room!")
            print data
            return

def Server_sent_msg(conn,nickname):
    global data
    while True:
        if cond.acquire():
            cond.wait()
            if data:
                try:
                    conn.send(data)
                    cond.release()
                except:
                    cond.release()
                    return

while True :
    #wait to accept a connection
    conn , addr = s.accept()
    print 'Got connection from ',addr[0] + ':' + str(addr[1])
    nickname = conn.recv(1024) #client should sent server a nickname as soon as connected.
    NotifyAll('Welcome ' + nickname + ' to the room!')
    print data
    print str((threading.activeCount() + 1) / 2) + ' person(s)!'
    conn.send(data)
    threading.Thread(target = Server_recv_msg , args = (conn, nickname)).start()
    threading.Thread(target = Server_sent_msg , args = (conn, nickname)).start()



s.close()
