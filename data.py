from helpers import tomorrow_date


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

class DataForCreationCourier:
    CREATION_COURIER_BODY = {
    "login": "qaa_courier",
    "password": "12345",
    "firstName": "sergei"
}

class DataForCreationOrder:
    CREATION_ORDER_BODY = {
    "firstName": "Sergei",
    "lastName": "Test",
    "address": "Konoha, 142 apt.",
    "metroStation": 7,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": tomorrow_date,
    "comment": "Hellow",
    "color": [
        "BLACK"
    ]
}