import hashlib
import re

def check_password(password):
    # Vérifie si la longueur du mot de passe est d'au moins 8 caractères
    if len(password) < 8:
        return False
    # Vérifie si le mot de passe contient au moins une lettre majuscule
    if not re.search(r'[A-Z]', password):
        return False
    # Vérifie si le mot de passe contient au moins une lettre minuscule
    if not re.search(r'[a-z]', password):
        return False
    # Vérifie si le mot de passe contient au moins un chiffre
    if not re.search(r'\d', password):
        return False
    # Vérifie si le mot de passe contient au moins un caractère spécial
    if not re.search(r'[!@#$%^&*]', password):
        return False
    # Si toutes les conditions sont remplies, retourne True
    return True

while True:
    # Demande à l'utilisateur de choisir un mot de passe
    password = input('Choisissez un mot de passe: ')
    # Vérifie si le mot de passe choisi respecte les exigences de sécurité
    if check_password(password):
        # Si le mot de passe est valide, affiche un message de confirmation et quitte la boucle while
        print('Mot de passe valide')
        break
    else:
        # Si le mot de passe n'est pas valide, affiche un message d'erreur et demande à l'utilisateur de choisir un nouveau mot de passe
        print('Mot de passe invalide. Veuillez réessayer.')

# Utilise la librairie hashlib et l'algorithme SHA-256 pour hacher le mot de passe choisi par l'utilisateur
hashed_password = hashlib.sha256(password.encode()).hexdigest()
# Affiche le mot de passe haché
print(f'Le mot de passe haché est: {hashed_password}')