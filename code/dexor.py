def xor_decrypt(message_crypte, cle):
    '''Cette fonction décrypte un message crypté par la méthode XOR en utilisant une clé'''
    bytes_cryptes = bytes.fromhex(message_crypte)
    bytes_cle = cle.encode()
    
    # Déchiffrer chaque octet du message chiffré avec la clé en utilisant XOR
    bytes_decryptes = bytes([byte_crypte ^ bytes_cle[i % len(bytes_cle)] for i, byte_crypte in enumerate(bytes_cryptes)])
    
    return bytes_decryptes.decode()

# Exemple d'utilisation
message_crypte = ""
cle = ""
message_decrypte = xor_decrypt(message_crypte, cle)
print(message_decrypte)
