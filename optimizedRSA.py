from gmpy2 import *
from random import *
import time

# 무작위 소수 p, q 구하기
while True:
    
    #p 구하기
    while True:

        state = gmpy2.random_state(randint(1, 10000000))
        p = random_number = gmpy2.mpz_urandomb(state, 1024)
        
        # 내장된 고성능 소수 판별 함수 사용 (Miller-Rabin 테스트)
        if gmpy2.is_prime(p):
            break
        
    #q 구하기
    while True:
        state = gmpy2.random_state(randint(1, 10000000))
        q = gmpy2.mpz_urandomb(state, 1024)
    
        if gmpy2.is_prime(q) and q != p:
            break
        
    break
print("p : ", end="")
print(p)
print("q : ", end="")
print(q)

#N 구하기
N = p*q
print("N : ", end="")
print(N)


#L 구하기
L = gmpy2.lcm(p - 1, q - 1)
print("L : ", end="")
print(L)


#E 구하기
while True:
    state = gmpy2.random_state(randint(1, 10000000))
    E = gmpy2.mpz_urandomb(state, 1024)
    if E < 1:
        continue
    
    if E < L:
        resultLcm = gmpy2.gcd(E, L)
        if resultLcm == 1:
            break
        
print("E : ", end="")
print(E)


# Find D
D = gmpy2.invert(E, L)
print("D : ", end="")
print(D)

# Simplify D using Fermat's little theorem
dP = gmpy2.f_mod(D, p - 1)
dQ = gmpy2.f_mod(D, q - 1)
qInv = gmpy2.invert(q, p)


############채팅############
from socket import *
import threading, pickle

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


            #@@@ 복호화 시간 측정 시작
            start_time = time.perf_counter()

            for En in data:

                #@@@ Decrypting using the CRT 
                m1 = gmpy2.powmod(En, dP, p)
                m2 = gmpy2.powmod(En, dQ, q)

                #@@@ Garner's algorithm
                h = (qInv * (m1 - m2)) % p
                M = m2 + h * q
                
                decryptedL.append(chr(M))

            #@@@ 복호화 시간 종료    
            end_time = time.perf_counter()
            duration = end_time - start_time
            
            dataDecrypted = "".join(decryptedL)

            print(f'\nChat partner : {dataDecrypted} (Decryption: {duration:.5f}s)\n')
        else : pass

port = int(input("port : "))
serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', port))
serverSock.listen(1)

connectionSock, addr = serverSock.accept()

print(str(addr),'에서 접속이 확인되었습니다.')

sender = threading.Thread(target=send, args=(connectionSock,))
receiver = threading.Thread(target=receive, args=(connectionSock,))

sender.start()
receiver.start()