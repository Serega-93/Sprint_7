import allure

from order_methods import OrderMethods


class TestReceivingListOrders:

    @allure.title("Успешное получение списка заказов")
    def test_successful_receiving_list_orders(self):
        with allure.step("Получение списка заказов"):
            response = OrderMethods.receiving_list_orders()
            response_body = response.json()
            assert response.status_code == 200 and "orders" in response_body
