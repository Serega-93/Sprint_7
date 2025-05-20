import requests

from data import Url


class OrderMethods:
    @staticmethod
    def creation_order(body):
        number_track = requests.post(f'{Url.BASE_URL}{Url.CREATION_ORDER}', json=body)
        return number_track.json()["track"]

    @staticmethod
    def receiving_order_by_number(track):
        params = {"t": track}
        order_id = requests.get(f'{Url.BASE_URL}{Url.RECEIVING_ID_COURIER}', params=params)
        return order_id.json()["order"][0]["id"]

    @staticmethod
    def accept_the_order(track, courier_id):
        params = {"courierId": courier_id}
        return requests.put(f'{Url.BASE_URL}{Url.ACCEPT_THE_ORDER}/{track}', params=params)

    @staticmethod
    def receiving_list_orders(courier_id):
        params = {"courierId": courier_id}
        return requests.get(f'{Url.BASE_URL}{Url.RECEIVING_LIST_ORDERS}', params=params)

    @staticmethod
    def cancel_order(track):
        params = {"track": track}
        return requests.put(f'{Url.BASE_URL}{Url.CANCEL_ODER}', params=params)
