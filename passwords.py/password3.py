import json
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def add_password(passwords, service, password):
    passwords[service] = hash_password(password)
    with open('passwords.json', 'w') as f:
        json.dump(passwords, f)

#gestion d'exception pour ouverture et retour d'afficher json
def get_passwords():
    try:
        with open('passwords.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def main():
    passwords = get_passwords()
    while True:
        action = input('Enter "add" to add a password or "show" to show all passwords: ')
        if action == 'add':
            service = input('Enter the name of the service: ')
            password = input('Enter the password: ')
            add_password(passwords, service, password)
        elif action == 'show':
            for service, password in passwords.items():
                print(f'{service}: {password}')
        else:
            break

if __name__ == '__main__':
    main()