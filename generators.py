from faker import Faker
from helpers import tomorrow_date


fake = Faker()

def generation_data_courier():
    return {
    "login": fake.login(),
    "password": fake.password(length=5),
    "firstName": fake.first_name()
}
