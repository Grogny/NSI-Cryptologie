# Importation du module 'socket' pour la communication réseau
import socket

# Fonction pour envoyer la clé publique au serveur
def send_public_key(public_key_file_path, server_ip, server_port):
    # Lecture de la clé publique depuis le fichier
    with open(public_key_file_path, "rb") as public_key_file:
        public_key = public_key_file.read()

    # Établissement d'une connexion avec le serveur via un socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Connexion au serveur à l'adresse IP et au port spécifiés
        s.connect((server_ip, server_port))
        # Envoi de la clé publique au serveur
        s.sendall(public_key)

    # Affichage d'un message indiquant que la clé publique a été envoyée avec succès
    print("Clé publique envoyée au serveur.")

# Bloc d'exécution principal
if __name__ == "__main__":
    # Spécification du chemin du fichier contenant la clé publique
    public_key_file_path = "public_key.pem"
    # Spécification de l'adresse IP du serveur
    server_ip = "5.196.162.85"
    # Spécification du port utilisé par le serveur
    server_port = 12345

    # Appel de la fonction pour envoyer la clé publique au serveur
    send_public_key(public_key_file_path, server_ip, server_port)
'''

    Le module socket est utilisé pour permettre la communication sur le réseau.
    La fonction send_public_key prend en paramètres le chemin du fichier contenant la clé publique, l'adresse IP du serveur, et le port sur lequel le serveur écoute.
    La clé publique est lue à partir du fichier spécifié.
    Un socket est créé et connecté au serveur à l'adresse IP et au port spécifiés.
    La clé publique est ensuite envoyée au serveur via le socket.
    Un message est affiché pour indiquer que la clé publique a été envoyée avec succès.

'''