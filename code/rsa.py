import random
import math

def test_miller_rabin(p):
    "Implémentation du test de primalité de Miller Rabin avec p : int (voir compte rendu)"
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
    "Implémentation de l'algorithme étendu d'euclide avec a : int; b : int (voir compte rendu)"
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
    """Implémentation de l'algorithme d'exponentiation modulaire avec base : int; exp : int; module : int (voir compte rendu)"""
    result = 1
    while exp > 0:
        if exp & 1 > 0:
            result = (result * base) % module
        exp >>= 1
        base = (base * base) % module
    return result


def genclef() :
    """Programme en charge de la génération des clefs (voir compte rendu)"""
    p = random.randint(10**8, 10**9)
    q = random.randint(10**8, 10**9)
    
    while not test_miller_rabin(p)==True :
        p = random.randint(10**8, 10**9)
        
    while not test_miller_rabin(q)==True :
        q = random.randint(10**8, 10**9)

    global module_chiffrement
    module_chiffrement = p*q
    
    global phi
    phi = (p-1)*(q-1)
    
    global exposant_chiffrement
    exposant_chiffrement = 65537
    
    global exposant_déchiffrement
    exposant_déchiffrement = trouve_d(exposant_chiffrement, phi)
    
    clef_pub = [module_chiffrement,exposant_chiffrement]
    clef_prv = [module_chiffrement,exposant_déchiffrement]
    
    return(clef_pub, clef_prv)

def chiffrement(m) :
    """Chiffrement du message ..."""
    m_1 = ord(m)
    c = expmodulaire(m_1, exposant_chiffrement, module_chiffrement)
    return c

def dechiffrement(c, d, n) :
    """Déchiffrement du message ..."""
    m = expmodulaire(c,d,n)
    return chr(m)

choix = int(input("Souhaitez-vous chiffrer votre message (select 1) ou le déchiffrer (select 2) ? "))
if choix == 1:
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
    c = int(input("Quel code souhaitez-vous déchiffrer ? "))
    d = int(input("Quel exposant de déchiffrement avez-vous ? "))
    n = int(input("Quel est votre module de chiffrement ? "))
    print(f'Votre message est {dechiffrement(c, d, n)}')
