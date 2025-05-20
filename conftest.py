import pytest

from courier_methods import CourierMethods
from data import DataForCreationCourier
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