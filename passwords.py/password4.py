def check_password(file_path, password):
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip() == password:
                return True
    return False

file_path = 'passwords.txt'
password = 'mon_mot_de_passe'

if check_password(file_path, password):
    print('Le mot de passe est déjà enregistré dans le fichier.')
else:
    print('Le mot de passe n\'est pas enregistré dans le fichier.')