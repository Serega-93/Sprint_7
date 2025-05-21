import allure
import requests

from data import Url


class OrderMethods:
    @staticmethod
    @allure.title("Создаём заказ")
    def creation_order(body):
        number_track = requests.post(f'{Url.BASE_URL}{Url.CREATION_ORDER}', json=body)
        return number_track

    @staticmethod
    @allure.title("Получаем id заказа по номеру")
    def receiving_id_order_by_number(track):
        params = {"t": track}
        order_id = requests.get(f'{Url.BASE_URL}{Url.RECEIVING_ORDER_BY_NUMBER}', params=params)
        return order_id

    @staticmethod
    @allure.title("Принять заказ")
    def accept_the_order(order_id, courier_id):
        if order_id:
            url = f'{Url.BASE_URL}{Url.ACCEPT_THE_ORDER}/{order_id}'
            params = {"courierId": courier_id}
        else:
            url = f'{Url.BASE_URL}{Url.ACCEPT_THE_ORDER}/courierId={courier_id}'
            params = None
        return requests.put(url, params=params)

    @staticmethod
    @allure.title("Получаем список заказов")
    def receiving_list_orders():
        return requests.get(f'{Url.BASE_URL}{Url.RECEIVING_LIST_ORDERS}')

    @staticmethod
    @allure.title("Отменяем заказ")
    def cancel_order(track):
        params = {"track": track}
        return requests.put(f'{Url.BASE_URL}{Url.CANCEL_ODER}', params=params)
