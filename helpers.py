import random
import string


def generate_email():
    email = f'Andrey_Bakhtin_47{random.randint(100,999)}@yandex.ru'
    return email

def generate_password():
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    return password

def get_user_data():
    email = generate_email()
    password = generate_password()
    name = 'Андрей'
    return {'email': email, 'password': password, 'name': name}
