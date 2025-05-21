

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

class DataResponse:
    TWO_HUNDRED_OK = {"ok":True}
    FOUR_HUNDRED_ERROR = {'code': 400, 'message': 'Недостаточно данных для поиска'}
    FOUR_HUNDRED_FOUR_ERROR_ORDER_NOT_EXIST = {'code': 404, 'message': 'Заказа с таким id не существует'}
    FOUR_HUNDRED_FOUR_ERROR_COURIER_NOT_EXIST = {'code': 404, 'message': 'Курьера с таким id не существует'}
    FOUR_HUNDRED_FOUR_ERROR_COURIER_NOT_ID = {"code": 404, "message": "Курьера с таким id нет."}
    FOUR_HUNDRED_FOUR_ERROR_ORDER_NOT_FOUND = {'code': 404, 'message': 'Заказ не найден'}
