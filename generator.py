import random

class DataForCreationCourier:

    @staticmethod
    def generate_body():
        return {
            "login": f"test_login_{random.randint(1000, 9999)}",
            "password": f"{random.randint(1000, 9999)}",
            "firstName": "sergei"
    }