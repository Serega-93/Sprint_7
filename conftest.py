import pytest

from courier_methods import CourierMethods
from data import DataForCreationCourier


@pytest.fixture
def generation_courier_data():
    courier_body = DataForCreationCourier.CREATION_COURIER_BODY
    login = courier_body["login"]
    password = courier_body["password"]
    yield [courier_body, login, password]
    courier_id = CourierMethods.receiving_id_courier(login, password)
    CourierMethods.deleted_courier(courier_id)
