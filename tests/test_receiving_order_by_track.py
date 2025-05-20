import allure

from data import DataForCreationOrder
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
            assert response.status_code == 200 and "order" in response_data
            request.node.funcargs["cleanup_order"] = track

    @allure.title("Ошибка при получении заказа без номера")
    def test_error_receiving_order_without_track(self, cleanup_order, request):
        with allure.step("Создаём заказ"):
            body = DataForCreationOrder.CREATION_ORDER_BODY
            track = OrderMethods.creation_order(body).json()["track"]
        with allure.step("Получение заказа"):
            response = OrderMethods.receiving_id_order_by_number(None)
            response_data = response.json()
            assert response_data == {'code': 400, 'message': 'Недостаточно данных для поиска'}
            request.node.funcargs["cleanup_order"] = track

    @allure.title("Ошибка при получении заказа c несуществующим номером")
    def test_error_receiving_order_non_existent_track(self, cleanup_order, request):
        with allure.step("Создаём заказ"):
            body = DataForCreationOrder.CREATION_ORDER_BODY
            track = OrderMethods.creation_order(body).json()["track"]
        with allure.step("Получение заказа"):
            response = OrderMethods.receiving_id_order_by_number(999999)
            response_data = response.json()
            assert response_data == {'code': 404, 'message': 'Заказ не найден'}
            request.node.funcargs["cleanup_order"] = track

