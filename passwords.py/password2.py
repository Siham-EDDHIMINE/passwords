import re
import hashlib

def check_password(password):
    if len(password) < 8:
        print("Le mot de passe doit contenir au moins 8 caractères.")
        return False
    if not re.search(r"[A-Z]", password):
        print("Le mot de passe doit contenir au moins une lettre majuscule.")
        return False
    if not re.search(r"[a-z]", password):
        print("Le mot de passe doit contenir au moins une lettre minuscule.")
        return False
    if not re.search(r"\d", password):
        print("Le mot de passe doit contenir au moins un chiffre.")
        return False
    if not re.search(r"[!@#$%^&*]", password):
        print("Le mot de passe doit contenir au moins un caractère spécial (!, @, #, $, %, ^, &, *).")
        return False
    return True

password = input("Choisissez un mot de passe : ")
while not check_password(password):
    password = input("Choisissez un nouveau mot de passe : ")

print("Mot de passe valide !")

hashed_password = hashlib.sha256(password.encode()).hexdigest()
print(f"Mot de passe crypté : {hashed_password}")