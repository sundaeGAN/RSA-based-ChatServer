from socket import *
import threading, gmpy2, pickle

def send(sock):
    while True:
        encryptedL = []

        Message = list(input(""))
        
        for M in Message:
            encryptedL.append(gmpy2.powmod(ord(M), E, N))
        
        data = pickle.dumps(encryptedL)
        
        sock.sendall(data)
    
def receive(sock):
    while True:
        data = sock.recv(4096)

        if data :
            data = pickle.loads(data)
            
            decryptedL = []
            decryptedL2 = []
            
            for En in data:
                decryptedL.append(gmpy2.powmod(En, D, N))
                
            for de in decryptedL:
                decryptedL2.append(chr(de))

            dataDecrypted = "".join(decryptedL2)
            
            print('\n상대방 : ' + dataDecrypted + '\n')
        else : pass

ip = input("IP : ")
port = int(input("port : "))
E = int(input("E : "))
D = int(input("D : "))
N = int(input("N : "))

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect((ip, port))
print('연결 확인 됐습니다.')

sender = threading.Thread(target=send, args=(clientSock,))
receiver = threading.Thread(target=receive, args=(clientSock,))

sender.start()
receiver.start()