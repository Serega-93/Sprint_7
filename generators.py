from faker import Faker
from helpers import tomorrow_date


fake = Faker()

def generation_data_courier():
    return {
    "login": fake.login(),
    "password": fake.password(length=5),
    "firstName": fake.first_name()
}

def generation_data_order():
    address = fake.street_address()
    address = (address.replace("(", "").replace(")", "").replace("/", ''))
    phone = fake.phone_number()
    phone = (phone.replace("-", "").replace(" ", "").replace("(", "")
             .replace(")", ""))
    phone = "8" + phone[1:]
    return {
    "firstName": fake.first_name(),
    "lastName": fake.last_name(),
    "address": address,
    "metroStation": fake.random_int(min=1, max=237),
    "phone": phone,
    "rentTime": fake.random_int(min=1, max=7),
    "deliveryDate": tomorrow_date,
    "comment": fake.sentence(),
    "color": [
        "BLACK"
    ]
}