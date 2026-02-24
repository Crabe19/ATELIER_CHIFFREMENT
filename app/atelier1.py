import os
from cryptography.fernet import Fernet
import sys

# Récupération de la clé depuis l'environnement
key = os.getenv("MY_FERNET_KEY")

if not key:
    print("Erreur : La variable d'environnement MY_FERNET_KEY est absente.")
    sys.exit(1)

f = Fernet(key.encode())

def process_file(action, input_file, output_file):
    with open(input_file, "rb") as file:
        data = file.read()
    
    if action == "encrypt":
        result = f.encrypt(data)
    else:
        result = f.decrypt(data)
        
    with open(output_file, "wb") as file:
        file.write(result)
    print(f"Succès : {input_file} -> {output_file}")

if __name__ == "__main__":
    # Usage: python app/fernet_atelier1.py encrypt secret.txt secret.enc
    mode = sys.argv[1]
    in_f = sys.argv[2]
    out_f = sys.argv[3]
    process_file(mode, in_f, out_f)