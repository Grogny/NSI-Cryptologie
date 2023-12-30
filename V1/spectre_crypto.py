from nacl.secret import SecretBox
from nacl.utils import random

def encrypt_message(key, plaintext):
    box = SecretBox(key)
    nonce = random(SecretBox.NONCE_SIZE)
    ciphertext = box.encrypt(plaintext.encode('utf-8'), nonce)
    return nonce + ciphertext

def decrypt_message(key, ciphertext):
    box = SecretBox(key)
    nonce = ciphertext[:SecretBox.NONCE_SIZE]
    decrypted = box.decrypt(ciphertext[SecretBox.NONCE_SIZE:])
    return decrypted.decode('utf-8')

# Générer une clé aléatoire de 32 octets
key = random(SecretBox.KEY_SIZE)

# Saisir le message de l'utilisateur
message = input('Entrez votre message: ')

# Chiffrer le message
encrypted_message = encrypt_message(key, message)
print(f"Message chiffré: {encrypted_message.hex()}")

# Enregistrer le message chiffré dans un fichier
with open("message.txt", "wb") as fichier:
    fichier.write(encrypted_message)
print("ceci est la clé:",key)
