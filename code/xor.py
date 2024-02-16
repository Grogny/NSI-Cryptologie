def xor_encrypt(message, cle):
    '''Cette fonction crypte un message en utilisant une clé (technique XOR)'''
    # Convertir le message et la clé en bytes
    bytes_message = message.encode()
    bytes_cle = cle.encode()
    
    # Chiffrer chaque octet du message avec la clé en utilisant XOR
    bytes_cryptes = bytes([octet_message ^ bytes_cle[i % len(bytes_cle)] for i, octet_message in enumerate(bytes_message)])
    
    # Retourner le message chiffré sous forme de chaîne hexadécimale
    return bytes_cryptes.hex()  # Convertir les bytes en hexadécimal pour faciliter le stockage et la lecture


message = ""
cle = ""
message_crypte = xor_encrypt(message, cle)
print(message_crypte)
