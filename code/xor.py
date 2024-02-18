def chiffrement_xor(message, cle):
    '''Cette fonction crypte un message en utilisant une clé (technique XOR)'''
    # Convertir le message et la clé en bytes
    bytes_message = message.encode()
    bytes_cle = cle.encode()
    
    # Chiffrer chaque octet du message avec la clé en utilisant XOR
    bytes_cryptes = bytes([octet_message ^ bytes_cle[i % len(bytes_cle)] for i, octet_message in enumerate(bytes_message)])
    
    # Retourner le message chiffré sous forme de chaîne hexadécimale
    return bytes_cryptes.hex()  # Convertir les bytes en hexadécimal pour faciliter le stockage et la lecture


def dechiffrement_xor(message_crypte, cle):
    '''Cette fonction décrypte un message crypté par la méthode XOR en utilisant une clé'''
    bytes_cryptes = bytes.fromhex(message_crypte)
    bytes_cle = cle.encode()
    
    # Déchiffrer chaque octet du message chiffré avec la clé en utilisant XOR
    bytes_decryptes = bytes([byte_crypte ^ bytes_cle[i % len(bytes_cle)] for i, byte_crypte in enumerate(bytes_cryptes)])
    
    return bytes_decryptes.decode()

# Exemple d'utilisation
# message = "ELOUAN"
# message_crypte = "06000a160d0b"
# cle = "CLE"

# message_crypte = chiffrement_xor(message, cle)
# message_decrypte = dechiffrement_xor(message_crypte, cle)
# print(message_crypte)
# print(message_decrypte)