def xor_decrypt(encrypted_message, key):
    '''cette fonction decrypte un message crypter par la methode XOR en renant une clé et un message '''
    encrypted_bytes = bytes.fromhex(encrypted_message)
    key_bytes = key.encode()
    
    # Déchiffrer chaque byte du message chiffré avec la clé en utilisant XOR
    decrypted_bytes = bytes([encrypted_byte ^ key_bytes[i % len(key_bytes)] for i, encrypted_byte in enumerate(encrypted_bytes)])
    
    return decrypted_bytes.decode()

# Exemple d'utilisation
encrypted_message = ""
key = ""
decrypted_message = xor_decrypt(encrypted_message, key)
print(decrypted_message)
