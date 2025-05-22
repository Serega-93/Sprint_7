import allure

from data import DataForCreationOrder, DataResponse
from order_methods import OrderMethods


class TestReceivingOrderByTrack:

    @allure.title("Успешное получение заказа по номеру")
    def test_successful_receiving_order(self, cleanup_order, request):
        with allure.step("Создаём заказ"):
            body = DataForCreationOrder.CREATION_ORDER_BODY
            track = OrderMethods.creation_order(body).json()["track"]
        with allure.step("Получение заказа"):
            response = OrderMethods.receiving_id_order_by_number(track)
            response_data = response.json()
            request.node.funcargs["cleanup_order"] = track
            assert response.status_code == 200 and "order" in response_data


    @allure.title("Ошибка при получении заказа без номера")
    def test_error_receiving_order_without_track(self, cleanup_order, request):
        with allure.step("Создаём заказ"):
            body = DataForCreationOrder.CREATION_ORDER_BODY
            track = OrderMethods.creation_order(body).json()["track"]
        with allure.step("Получение заказа"):
            response = OrderMethods.receiving_id_order_by_number(None)
            response_data = response.json()
            request.node.funcargs["cleanup_order"] = track
            assert response_data == DataResponse.FOUR_HUNDRED_ERROR


    @allure.title("Ошибка при получении заказа c несуществующим номером")
    def test_error_receiving_order_non_existent_track(self, cleanup_order, request):
        with allure.step("Создаём заказ"):
            body = DataForCreationOrder.CREATION_ORDER_BODY
            track = OrderMethods.creation_order(body).json()["track"]
        with allure.step("Получение заказа"):
            response = OrderMethods.receiving_id_order_by_number(999999)
            response_data = response.json()
            request.node.funcargs["cleanup_order"] = track
            assert response_data == DataResponse.FOUR_HUNDRED_FOUR_ERROR_ORDER_NOT_FOUND
