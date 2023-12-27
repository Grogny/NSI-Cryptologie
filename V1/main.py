from colorama import Fore

import argparse
import colorama

def main():
    colorama.init()
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--aes", help="Méthode de cryptage avec AES (Advanced Encryption Standard), clé secrete", dest='aes_cryptage')
    parser.add_argument("-r", "--rsa", help="Méthode de cryptage avec RSA (Rivest, Shamir, Adleman), clé publique", dest='rsa_cryptage')
    parser.add_argument("-s", "--s20", help="Méthode de cryptage avec Salsa20", dest='salsa20_cryptage')

    parser.add_argument("-da", "--daes", help="Méthode de decryptage avec AES (Advanced Encryption Standard), clé secrete", dest='aes_decryptage')
    parser.add_argument("-dr", "--drsa", help="Méthode de decryptage avec RSA (Rivest, Shamir, Adleman), clé publique", dest='rsa_decryptage')
    parser.add_argument("-ds", "--ds20", help="Méthode de decryptage avec Salsa20", dest='salsa20_decryptage')
    args = parser.parse_args()

    print(f"""
    {Fore.BLUE}███╗   ██╗{Fore.WHITE}███████╗{Fore.RED}██╗    {Fore.GREEN} ██████╗██████╗ ██╗   ██╗██████╗ ████████╗ ██████╗ ██╗      ██████╗  ██████╗ ██╗███████╗
    {Fore.BLUE}████╗  ██║{Fore.WHITE}██╔════╝{Fore.RED}██║    {Fore.GREEN}██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██╔═══██╗██║     ██╔═══██╗██╔════╝ ██║██╔════╝
    {Fore.BLUE}██╔██╗ ██║{Fore.WHITE}███████╗{Fore.RED}██║    {Fore.GREEN}██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   ██║   ██║██║     ██║   ██║██║  ███╗██║█████╗  
    {Fore.BLUE}██║╚██╗██║{Fore.WHITE}╚════██║{Fore.RED}██║    {Fore.GREEN}██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ██║   ██║██║     ██║   ██║██║   ██║██║██╔══╝  
    {Fore.BLUE}██║ ╚████║{Fore.WHITE}███████║{Fore.RED}██║    {Fore.GREEN}╚██████╗██║  ██║   ██║   ██║        ██║   ╚██████╔╝███████╗╚██████╔╝╚██████╔╝██║███████╗
    {Fore.BLUE}╚═╝  ╚═══╝{Fore.WHITE}╚══════╝{Fore.RED}╚═╝    {Fore.GREEN} ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝    ╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚══════╝                                                                                                              

    Utilisation :
    python3 [-CRYPTAGE/DECRYPTAGE METHODE] [-MESSAGE]

    -h / --help pour plus d'informations.

    """)

if __name__ == "__main__":
    main()