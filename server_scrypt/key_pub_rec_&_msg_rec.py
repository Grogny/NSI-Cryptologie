# Importation du module 'socket' pour la communication réseau
import socket

# Fonction pour recevoir des données du client
def receive_data(server_ip, server_port):
    # Création d'un socket pour l'écoute
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Attribution de l'adresse IP et du port au socket
        s.bind((server_ip, server_port))
        # Mise en écoute du socket
        s.listen()
        # Attente d'une connexion entrante
        conn, addr = s.accept()
        # Gestion de la connexion
        with conn:
            # Réception des données du client (4096 octets à la fois)
            data = conn.recv(4096)
            return data

# Bloc d'exécution principal
if __name__ == "__main__":
    # Adresse IP du serveur (0.0.0.0 signifie écoute sur toutes les interfaces)
    server_ip = "0.0.0.0"
    # Port utilisé par le serveur
    server_port = 12345

    # Réception de la clé publique du client
    public_key_data = receive_data(server_ip, server_port)
    print("Clé publique reçue:", public_key_data.decode('utf-8'))

    # Réception du message chiffré du client
    encrypted_message_data = receive_data(server_ip, server_port)
    print("Message chiffré reçu:", encrypted_message_data.hex())
'''
    La fonction receive_data prend en paramètres l'adresse IP et le port sur lesquels le serveur écoute.
    Un socket est créé, lié à l'adresse IP et au port spécifiés, puis mis en écoute.
    Lorsqu'une connexion entrante est acceptée, la fonction récupère les données du client à travers cette connexion.
    Dans le bloc d'exécution principal, la fonction est utilisée pour recevoir la clé publique du client d'abord, puis le message chiffré.
    Les données reçues sont affichées à la console.
'''