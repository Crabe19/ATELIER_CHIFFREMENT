import sys
from nacl.secret import SecretBox
from nacl.utils import random

# On génère ou on utilise une clé de 32 octets
# Pour cet atelier, on en génère une fixe (en prod, utilisez un secret)
SHARED_KEY = b'\x1c' * 32 
box = SecretBox(SHARED_KEY)

def encrypt_file(input_path, output_path):
    with open(input_path, "rb") as f:
        message = f.read()
    
    # SecretBox génère un 'nonce' (IV) aléatoire automatiquement
    encrypted = box.encrypt(message)
    
    with open(output_path, "wb") as f:
        f.write(encrypted)
    print(f"Chiffré avec PyNaCl dans {output_path}")

def decrypt_file(input_path, output_path):
    with open(input_path, "rb") as f:
        encrypted_data = f.read()
    
    # Le nonce est stocké au début du message chiffré par PyNaCl
    decrypted = box.decrypt(encrypted_data)
    
    with open(output_path, "wb") as f:
        f.write(decrypted)
    print(f"Déchiffré avec PyNaCl dans {output_path}")

if __name__ == "__main__":
    action = sys.argv[1] # encrypt ou decrypt
    if action == "encrypt":
        encrypt_file(sys.argv[2], sys.argv[3])
    elif action == "decrypt":
        decrypt_file(sys.argv[2], sys.argv[3])