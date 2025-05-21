import allure
import pytest

from data import DataForCreationOrder
from order_methods import OrderMethods


class TestCreatingOrder:

    @pytest.mark.parametrize("color", [ [], ["BLACK"], ["GREY"], ["BLACK", "GREY"]])
    @allure.title("Успешное создание заказа")
    def test_successful_creating_order(self, cleanup_order, color, request):
        with allure.step("Создаём заказ"):
            body = DataForCreationOrder.CREATION_ORDER_BODY.copy()
            body["color"] = color
            response = OrderMethods.creation_order(body)
            track = response.json()["track"]
            assert response.status_code == 201
            assert track is not None

        request.node.funcargs["cleanup_order"] = track
