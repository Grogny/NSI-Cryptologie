# Importation des modules nécessaires de la bibliothèque cryptography
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa


# Fonction pour générer une paire de clés RSA (publique et privée)
def generate_key_pair():
    # Génération de la clé privée RSA
    private_key = rsa.generate_private_key(
        public_exponent=65537,  # Exposant public recommandé pour la sécurité
        key_size=2048  # Taille de la clé, plus grande pour plus de sécurité
    )

    # Obtention de la clé publique correspondante
    public_key = private_key.public_key()

    # Conversion de la clé privée en format PEM sans chiffrement (NoEncryption)
    private_key_bytes = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,  # Format PEM
        format=serialization.PrivateFormat.PKCS8,  # Format de clé privée PKCS8
        encryption_algorithm=serialization.NoEncryption()  # Aucun chiffrement
    )

    # Conversion de la clé publique en format PEM
    public_key_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,  # Format PEM
        format=serialization.PublicFormat.SubjectPublicKeyInfo  # Format de clé publique
    )

    # Retourne les clés privée et publique sous forme de bytes
    return private_key_bytes, public_key_bytes


# Bloc d'exécution principal
if __name__ == "__main__":
    # Appel de la fonction pour générer une paire de clés
    private_key, public_key = generate_key_pair()

    # Enregistrement de la clé privée dans un fichier "private_key.pem"
    with open("private_key.pem", "wb") as private_key_file:
        private_key_file.write(private_key)

    # Enregistrement de la clé publique dans un fichier "public_key.pem"
    with open("public_key.pem", "wb") as public_key_file:
        public_key_file.write(public_key)

    # Affichage d'un message indiquant que les paires de clés ont été générées et enregistrées
    print("Paires de clés générées et enregistrées.")
