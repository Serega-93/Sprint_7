

from helpers import TOMORROW_DATE


class Url:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru' # адрес сервера
    CREATION_COURIER = '/api/v1/courier' # Создание курьера
    RECEIVING_ID_COURIER = '/api/v1/courier/login' # Получение id курьера
    DELETE_COURIER = '/api/v1/courier'  # Удалить курьера
    CREATION_ORDER = '/api/v1/orders' # Создание заказа
    RECEIVING_ORDER_BY_NUMBER = '/api/v1/orders/track' # Получение id заказа по его номеру
    ACCEPT_THE_ORDER = '/api/v1/orders/accept' # Принять заказ
    RECEIVING_LIST_ORDERS = '/api/v1/orders' # Получение списка заказов
    CANCEL_ODER = '/api/v1/orders/cancel' # Отменить заказ

class NonExistentDataCourier:
    NON_EXISTENT_COURIER_BODY = {
        "login": "non_existent",
        "password": "11111"
    }

class DataForCreationOrder:
    CREATION_ORDER_BODY = {
    "firstName": "Sergei",
    "lastName": "Test",
    "address": "Konoha, 142 apt.",
    "metroStation": 7,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": TOMORROW_DATE,
    "comment": "Hellow",
    "color": []
}