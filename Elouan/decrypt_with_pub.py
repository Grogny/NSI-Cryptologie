# Importation du module 'socket' pour la communication réseau
import socket

# Importation des modules de cryptography pour la gestion du chiffrement
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

# Fonction pour recevoir des données du serveur
def receive_data(server_ip, server_port):
    # Création d'un socket pour la connexion au serveur
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Connexion au serveur à l'adresse IP et au port spécifiés
        s.connect((server_ip, server_port))
        # Réception des données du serveur (4096 octets à la fois)
        data = s.recv(4096)
        return data

# Fonction pour décrypter un message reçu du serveur
def decrypt_message(private_key_file_path, server_ip, server_port):
    # Réception du message chiffré du serveur
    encrypted_message_hex = receive_data(server_ip, server_port).decode('utf-8')
    encrypted_message = bytes.fromhex(encrypted_message_hex)

    # Lecture de la clé privée depuis le fichier
    with open(private_key_file_path, "rb") as private_key_file:
        private_key_bytes = private_key_file.read()

    # Chargement de la clé privée depuis les bytes
    private_key = serialization.load_pem_private_key(
        private_key_bytes,
        password=None  # Aucun mot de passe car la clé n'est pas chiffrée
    )

    # Déchiffrement du message avec la clé privée
    decrypted_message = private_key.decrypt(
        encrypted_message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Conversion du message déchiffré en chaîne de caractères
    return decrypted_message.decode('utf-8')

# Bloc d'exécution principal
if __name__ == "__main__":
    # Chemin du fichier contenant la clé privée
    private_key_file_path = "private_key.pem"
    # Adresse IP du serveur
    server_ip = "5.196.162.85"
    # Port utilisé par le serveur
    server_port = 12345

    # Appel de la fonction pour décrypter le message reçu du serveur
    decrypted_message = decrypt_message(private_key_file_path, server_ip, server_port)

    # Affichage du message déchiffré
    print("Message déchiffré:", decrypted_message)
'''
    La fonction receive_data est utilisée pour recevoir le message chiffré du serveur.
    Le message chiffré est ensuite déchiffré en utilisant la clé privée spécifiée dans le fichier.
    Les données reçues sont affichées à la console sous forme de message déchiffré.
'''