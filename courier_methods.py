import allure
import requests

from data import Url


class CourierMethods:

    @staticmethod
    @allure.title("Создаём курьера")
    def created_courier(body):
        return requests.post(f'{Url.BASE_URL}{Url.CREATION_COURIER}', json=body)

    @staticmethod
    @allure.title("Получаем id курьера")
    def receiving_id_courier(login, password):
        body = {
        "login": login,
        "password": password
        }
        response = requests.post(f'{Url.BASE_URL}{Url.RECEIVING_ID_COURIER}', json=body)
        return response

    @staticmethod
    @allure.title("Удаляем курьера")
    def deleted_courier(courier_id):
        return requests.delete(f'{Url.BASE_URL}{Url.DELETE_COURIER}/{courier_id}')
