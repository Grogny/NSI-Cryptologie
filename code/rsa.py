import random
import math

def estprime(p):
    k=0
    p_1=p-1
    
    while p_1%2==0 :
        p_1//=2
        k+=1
    
    for i in range(25) :
        a = random.randint(2, p-2)
        a_1 = expmodulaire(a,p_1,p)

        var = False
        if (a_1 == 1 or a_1 == p-1) :
            var = True
            return(var)
 
def gcd_etendu(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = gcd_etendu(b, a % b)
        return gcd, y, x - (a // b) * y

def trouve_d(e, phi):
    gcd, d, _ = gcd_etendu(e, phi)
    d = d % phi
    return d

   
    
def expmodulaire(base, exp, module):
    result = 1
    while exp > 0:
        if exp & 1 > 0:
            result = (result * base) % module
        exp >>= 1
        base = (base * base) % module
    return result


def genclef() :
    p = random.randint(10**8, 10**9)
    q = random.randint(10**8, 10**9)
    
    while not estprime(p)==True :
        p = random.randint(10**8, 10**9)
        
    while not estprime(q)==True :
        q = random.randint(10**8, 10**9)

    global n
    n = p*q
    
    global phi
    phi = (p-1)*(q-1)
    
    global e
    e = 65537
    
    global d
    d = trouve_d(e, phi)
    
    clef_pub = [n,e]
    clef_prv = [n,d]
    
    return(clef_pub, clef_prv)

def chiffrement(m) :
    m_1 = ord(m)
    c = expmodulaire(m_1, e, n)
    return c

def dechiffrement(c, d, n) :
    m = expmodulaire(c,d,n)
    return chr(m)

g = int(input("Souhaitez-vous chiffrer votre message (select 1) ou le déchiffrer (select 2) ? "))
if g == 1:
    chiff = input("Entrez votre message : ")
    m = []
    count=0
    for i in chiff :
        m.append(i)
    for i in range(len(m)) :
        result = genclef()
        f = chiffrement(m[i])
        count+=1
        print(f'Lettre {count} : Clef privée, Clef publique = {result}, et le chiffrement donne : {f}')

else :
    c = int(input("Quel message souhaitez-vous déchiffrer ? "))
    d = int(input("Quel exposant de déchiffrement avez-vous ?"))
    n = int(input("Quel est votre module de chiffrement ?"))
    print(f'Votre message est {dechiffrement(c, d, n)}')
