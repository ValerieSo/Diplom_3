import random
import string
from faker import Faker


class Generators:
    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @staticmethod
    def generate_random_email():
        fake = Faker(locale="ru_Ru")
        email = fake.email()
        return email

    @staticmethod
    def generate_random_password():
        password = Generators.generate_random_string(6)
        return password

    @staticmethod
    def generate_random_name():
        fake = Faker(locale="ru_Ru")
        name = fake.name()
        return name

    @staticmethod
    def generate_registration_user_data():
        email = Generators.generate_random_email()
        password = Generators.generate_random_password()
        name = Generators.generate_random_name()
        return {"email": email, "password": password, "name": name}
