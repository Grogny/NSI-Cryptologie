# Importation du module 'socket' pour la communication réseau
import socket

# Importation des modules de cryptography pour la gestion du chiffrement
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding

# Fonction pour chiffrer un message et l'envoyer au serveur
def encrypt_and_send_message(message, public_key_file_path, server_ip, server_port):
    # Lecture de la clé publique depuis le fichier
    with open(public_key_file_path, "rb") as public_key_file:
        public_key_bytes = public_key_file.read()

    # Chargement de la clé publique depuis les bytes
    public_key = serialization.load_pem_public_key(public_key_bytes)

    # Chiffrement du message avec la clé publique
    ciphertext = public_key.encrypt(
        message.encode('utf-8'),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Établissement d'une connexion avec le serveur via un socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Connexion au serveur à l'adresse IP et au port spécifiés
        s.connect((server_ip, server_port))
        # Envoi du message chiffré au serveur
        s.sendall(ciphertext)

    # Affichage d'un message indiquant que le message chiffré a été envoyé avec succès
    print("Message chiffré envoyé au serveur.")

# Bloc d'exécution principal
if __name__ == "__main__":
    # Message à chiffrer et envoyer
    message = "Hello, World!"
    # Chemin du fichier contenant la clé publique
    public_key_file_path = "public_key.pem"
    # Adresse IP du serveur
    server_ip = "5.196.162.85"
    # Port utilisé par le serveur
    server_port = 12345

    # Appel de la fonction pour chiffrer et envoyer le message au serveur
    encrypt_and_send_message(message, public_key_file_path, server_ip, server_port)
'''
    La fonction encrypt_and_send_message prend en paramètres le message à chiffrer, le chemin du fichier contenant la clé publique, l'adresse IP du serveur, et le port sur lequel le serveur écoute.
    La clé publique est lue à partir du fichier spécifié et chargée.
    Le message est chiffré avec la clé publique à l'aide de la méthode encrypt fournie par cryptography.
    Un socket est créé et connecté au serveur à l'adresse IP et au port spécifiés.
    Le message chiffré est envoyé au serveur via le socket.
    Un message est affiché pour indiquer que le message chiffré a été envoyé avec succès.

'''