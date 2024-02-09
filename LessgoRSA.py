import gmpy2
from random import *

# 무작위 소수 p, q 구하기
while True:
    
    #p 구하기
    while True:
        
        count = 0
        state = gmpy2.random_state(randint(1, 10000000))
        p = random_number = gmpy2.mpz_urandomb(state, 30)
        
        if p < 2 :
            continue;
        
        sqrtP = gmpy2.sqrt(random_number)
        
        i = 2
        while i <= sqrtP and count < 2:
            modP = gmpy2.f_mod(p, i)
            
            if modP != 0:
                pass
            elif modP == 0:
                count += 1
                
            i += 1
                
        if count >= 1:
            continue
        else : 
            break
        
    #q 구하기
    while True:
        
        count = 0
        state = gmpy2.random_state(randint(1, 10000000))
        q = random_number = gmpy2.mpz_urandomb(state, 30)
        
        if q < 2 :
            continue;
        
        sqrtQ = gmpy2.sqrt(random_number)
        
        i = 2
        while i <= sqrtQ and count < 2:
            modQ = gmpy2.f_mod(q, i)
            
            if modQ != 0:
                pass
            elif modQ == 0:
                count += 1
                
            i += 1
                
        if count >= 1:
            continue
        else : 
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
    E = gmpy2.mpz_urandomb(state, 30)
    if E < 1:
        continue
    
    if E < L:
        resultLcm = gmpy2.gcd(E, L)
        if resultLcm == 1:
            break
        
print("E : ", end="")
print(E)


#D 구하기
D = gmpy2.invert(E, L)
print("D : ", end="")
print(D)

##############암호화##############
M = int(input("Message : "))
encryptedM = gmpy2.powmod(M, E, N)
print("Encrypted Message : ", encryptedM)

##############복호화##############
decryptedM = gmpy2.powmod(encryptedM, D, N)
print("Decrypted Message : ", decryptedM)

        
    