import random
import string

def generer_mot_de_passe(longueur: int) -> str:
    caracteres = string.ascii_letters + string.digits + string.punctuation
    mot_de_passe = ''.join(random.choice(caracteres) for _ in range(longueur))
    return mot_de_passe
import hashlib

mot_de_passe = "motdepasse"
empreinte = hashlib.sha256(mot_de_passe.encode()).hexdigest()
print(empreinte)
longueur = 12
mot_de_passe = generer_mot_de_passe(longueur)
print(f"Mot de passe généré: {mot_de_passe}")