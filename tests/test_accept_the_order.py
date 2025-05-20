import allure

from order_methods import OrderMethods


class TestAcceptTheOrder:

    @allure.title("Успешное принятие заказа")
    def test_successful_accept_the_order(self, creating_courier_and_creating_order):
        with allure.step("Принятие заказа"):
            courier_id = creating_courier_and_creating_order[0]
            order_id = creating_courier_and_creating_order[1]
            response = OrderMethods.accept_the_order(order_id, courier_id).json()
            assert response == {"ok":True}

    @allure.title("Ошибка 400 при отправки запроса принятие заказа без id курьера")
    def test_error_accept_the_order_without_id_courier(self, creating_courier_and_creating_order):
        with allure.step("Принятие заказа"):
            courier_id = None
            order_id = creating_courier_and_creating_order[1]
            response = OrderMethods.accept_the_order(order_id, courier_id).json()
            assert response == {'code': 400, 'message': 'Недостаточно данных для поиска'}

    @allure.title("Ошибка 400 при отправки запроса принятие заказа без id заказа")
    def test_error_accept_the_order_without_id_order(self, creating_courier_and_creating_order):
        with allure.step("Принятие заказа"):
            courier_id = creating_courier_and_creating_order[0]
            order_id = None
            response = OrderMethods.accept_the_order(order_id, courier_id).json()
            assert response == {'code': 400, 'message': 'Недостаточно данных для поиска'}

    @allure.title("Ошибка 404 при отправки запроса принятие заказа с невалидным id заказа")
    def test_error_accept_the_order_invalid_id_order(self, creating_courier_and_creating_order):
        with allure.step("Принятие заказа"):
            courier_id = creating_courier_and_creating_order[0]
            order_id = 1
            response = OrderMethods.accept_the_order(order_id, courier_id).json()
            assert response == {'code': 404, 'message': 'Заказа с таким id не существует'}

    @allure.title("Ошибка 404 при отправки запроса принятие заказа с невалидным id курьера")
    def test_error_accept_the_order_invalid_id_courier(self, creating_courier_and_creating_order):
        with allure.step("Принятие заказа"):
            courier_id = 1
            order_id = creating_courier_and_creating_order[1]
            response = OrderMethods.accept_the_order(order_id, courier_id).json()
            assert response == {'code': 404, 'message': 'Курьера с таким id не существует'}