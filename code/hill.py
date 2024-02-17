import numpy as np # Le module 'NumPy' est utilisé pour manipuler des matrices

def lettre_vers_nombre(lettre):
    """La fonction "lettre_vers_nombre" renvoie la conversion de lettres en nombres. Par exemple : A=0, B=1, ..., Z=25"""
    return ord(lettre) - ord('A')

def nombre_vers_lettre(nombre):
    """La fonction "nombre_vers_lettre" renvoie la conversion de nombres en lettres. Par exemple : 0=A, 1=B, ..., 25=Z"""
    return chr(nombre + ord('A'))

def generer_matrice_cle(cle):
    """La fonction "generer_matrice_cle" transforme les caractères de la clé en leur équivalent en nombre par rapport Ã  leur rang
     dans l'alphabet pour ensuite remplir une matrice avec ces nombres. Cette matrice va être utilisée dans la suite du programme"""
    n = len(cle)
    taille = int(n ** 0.5) # Calcule la taille de la matrice clé en prenant la racine carrée entiére de la longueur de la clé. Cela garantit que la matrice clé est carrée et peut être remplie complétement avec les caractéres de la clé.
    if taille * taille < n:
        taille += 1
    cle_numerique = [lettre_vers_nombre(lettre) for lettre in cle]
    matrice_cle = np.zeros((taille, taille), dtype=int) # Remplissage d'une matrice à l'aide du module 'NumPy'
    for i in range(n):
        matrice_cle[i // taille, i % taille] = cle_numerique[i]
    return matrice_cle

def chiffrement_hill(message, matrice_cle):
    """La fonction "chiffrement_hill" effectue les calculs dÃ©taillÃ©s dans le compte rendu en s'aidant des fonctions précédentes
    de telle sorte à pouvoir chiffrer en Hill."""
    n = matrice_cle.shape[0]
    message_chiffre = ""
    message = message.upper().replace(" ", "")

    # Ajout de padding si nécessaire en remplaçant les trous par 'X'
    if len(message) % n != 0:
        message += 'X' * (n - len(message) % n)

    # Chiffrement par blocs de taille n
    for i in range(0, len(message), n):
        bloc = [lettre_vers_nombre(lettre) for lettre in message[i:i+n]]
        bloc_chiffre = np.dot(matrice_cle, np.array(bloc)) % 26
        message_chiffre += ''.join([nombre_vers_lettre(nombre) for nombre in bloc_chiffre])

    return message_chiffre

def dechiffrement_hill(message_chiffre, matrice_cle):
    """La fonction "dechiffrement_hill" effectue les calculs détaillés dans le compte rendu en s'aidant des fonctions précédentes
    de telle sorte à pouvoir déchiffrer un message qui a été chiffrer en Hill."""
    n = matrice_cle.shape[0]
    determinant = int(np.linalg.det(matrice_cle))
    print(determinant)

    # Calcul de l'inverse modulaire du déterminant
    inverse_modulaire = -1
    for i in range(26):
        if (determinant * i) % 26 == 1:
            inverse_modulaire = i
            break

    if inverse_modulaire == -1:
        raise ValueError("La matrice de clÃ© n'est pas inversible modulo 26")

    matrice_inverse = np.linalg.inv(matrice_cle) * determinant
    det_inv = inverse_modulaire % 26
    matrice_inverse = np.round(matrice_inverse * det_inv).astype(int) % 26

    message_dechiffre = ""

    for i in range(0, len(message_chiffre), n):
        bloc = [nombre_vers_lettre(int(x)) for x in np.dot(matrice_inverse, [lettre_vers_nombre(c) for c in message_chiffre[i:i+n]]) % 26]
        message_dechiffre += ''.join(bloc)

    return message_dechiffre

# Exemple d'utilisation
if __name__ == "__main__":

    """La méthode 'upper' permet de mettre la clé en lettres capitales, les lettres non capitales fonctionnent aussi mais donneront un résultat différent dû à l'UTF-8,
     quand Lester Sanders Hill invente sa méthode de chiffrement, l'UTF-8 n'existait pas, j'ai donc fait le choix d'être le plus fidèle à la méthode originelle :)"""
    cle = "bcdf".upper()
    message = "MARTEL"

    matrice_cle = generer_matrice_cle(cle)

    message_chiffre = chiffrement_hill(message, matrice_cle)
    message_dechiffre = dechiffrement_hill(message_chiffre, matrice_cle)

    print(f"Message chiffré : {message_chiffre}")
    print(f"Message déchiffré :{message_dechiffre}")
