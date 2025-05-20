import pytest

from courier_methods import CourierMethods
from generators import generation_data_courier, generation_data_order
from order_methods import OrderMethods


@pytest.fixture
def generation_courier_data():
    courier_body = generation_data_courier()
    login = courier_body["login"]
    password = courier_body["password"]
    yield [courier_body, login, password]
    courier_id = CourierMethods.receiving_id_courier(login, password)
    CourierMethods.deleted_courier(courier_id)
