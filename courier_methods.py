import requests

from data import Url


class CourierMethods:

    @staticmethod
    def created_courier(body):
        return requests.post(f'{Url.BASE_URL}{Url.CREATION_COURIER}', json=body)

    @staticmethod
    def receiving_id_courier(login, password):
        body = {
        "login": login,
        "password": password
        }
        response = requests.post(f'{Url.BASE_URL}{Url.RECEIVING_ID_COURIER}', json=body)
        return response

    @staticmethod
    def deleted_courier(courier_id):
        return requests.delete(f'{Url.BASE_URL}{Url.DELETE_COURIER}/{courier_id}')
