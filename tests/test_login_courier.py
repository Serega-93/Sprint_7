import allure
import pytest

from courier_methods import CourierMethods
from data import NonExistentDataCourier


class TestLoginCourier:

    @allure.title("Успешная авторизация курьером")
    def test_successful_authorization_courier(self, generation_courier_data):
        with allure.step("Создаём курьера"):
            CourierMethods.created_courier(generation_courier_data[0])
        with allure.step("Авторизуемся курьером"):
            login = generation_courier_data[1]
            password = generation_courier_data[2]
            response = CourierMethods.receiving_id_courier(login, password)
            response_data = response.json()
            assert response.status_code == 200 and "id" in response_data

    @pytest.mark.parametrize("login, password",
                              [("qaa_courier", "qa_courier"), ("1234", "12345")])
    @allure.title("Ошибка '404' при авторизации с неверным логином или паролем")
    def test_error_when_logging_in_with_an_incorrect_login_or_password(self, generation_courier_data, login, password):
        with allure.step("Создаём курьера"):
            CourierMethods.created_courier(generation_courier_data[0])
        with allure.step("Авторизуемся курьером"):
            response = CourierMethods.receiving_id_courier(login, password)
            assert response.status_code == 404

    @allure.title("Ошибка '404' при авторизации с несуществующем логином или паролем")
    def test_error_when_logging_in_with_an_incorrect_login_or_password(self, generation_courier_data):
        with allure.step("Создаём курьера"):
            CourierMethods.created_courier(generation_courier_data[0])
        with allure.step("Авторизуемся курьером"):
            login = NonExistentDataCourier.NON_EXISTENT_COURIER_BODY["login"]
            password = NonExistentDataCourier.NON_EXISTENT_COURIER_BODY["password"]
            response = CourierMethods.receiving_id_courier(login, password)
            assert response.status_code == 404

    @pytest.mark.parametrize("login, password",
                              [("qaa_courier", ""), ("", "12345")])
    @allure.title("Ошибка '400' при авторизации с пустым логином или паролем")
    def test_error_when_logging_in_with_an_empty_login_or_password(self, generation_courier_data, login, password):
        with allure.step("Создаём курьера"):
            CourierMethods.created_courier(generation_courier_data[0])
        with allure.step("Авторизуемся курьером"):
            response = CourierMethods.receiving_id_courier(login, password)
            assert response.status_code == 400
