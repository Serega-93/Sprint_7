import pytest

from courier_methods import CourierMethods
from data import DataForCreationCourier, DataForCreationOrder
from order_methods import OrderMethods


@pytest.fixture
def generation_courier_data():
    courier_body = DataForCreationCourier.CREATION_COURIER_BODY
    login = courier_body["login"]
    password = courier_body["password"]
    yield [courier_body, login, password]
    courier_id = CourierMethods.receiving_id_courier(login, password)
    value = courier_id.json()["id"]
    CourierMethods.deleted_courier(value)

@pytest.fixture
def cleanup_order(request):
    track = None
    yield track
    OrderMethods.cancel_order(track)

@pytest.fixture
def creating_courier_and_receiving_id():
    body = DataForCreationCourier.CREATION_COURIER_BODY
    CourierMethods.created_courier(body)
    login = body["login"]
    password = body["password"]
    courier_id = CourierMethods.receiving_id_courier(login, password).json()["id"]
    yield courier_id
    CourierMethods.deleted_courier(courier_id)

@pytest.fixture
def creating_courier_and_creating_order():
    courier_body = DataForCreationCourier.CREATION_COURIER_BODY
    CourierMethods.created_courier(courier_body)
    login = courier_body["login"]
    password = courier_body["password"]
    courier_id = CourierMethods.receiving_id_courier(login, password).json()["id"]
    order_body = DataForCreationOrder.CREATION_ORDER_BODY
    track = OrderMethods.creation_order(order_body).json()["track"]
    order_id = OrderMethods.receiving_id_order_by_number(track).json()["order"]["id"]
    yield [courier_id, order_id]
    CourierMethods.deleted_courier(courier_id)

