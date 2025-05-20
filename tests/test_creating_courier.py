import allure
import pytest

from courier_methods import CourierMethods
from generator import DataForCreationCourier


class TestCreatingCourier:

    @allure.title("Успешное создание курьера")
    def test_successful_creation_courier(self, generation_courier_data):
        with allure.step("Создаём курьера"):
            response = CourierMethods.created_courier(generation_courier_data[0])
            assert response.status_code == 201 and response.json() == {"ok": True}

    @allure.title("Ошибка '409' при создании двух одинаковых курьеров")
    def test_error_when_creating_two_identical_couriers(self, generation_courier_data):
        with allure.step("Создаём двух одинаковых курьеров"):
            response = CourierMethods.created_courier(generation_courier_data[0])
            response = CourierMethods.created_courier(generation_courier_data[0])
            assert response.status_code == 409

    @pytest.mark.parametrize("field, value", [("login", ""),("password", "")])
    @allure.title("Ошибка '400' при создании курьера с пустым обязательным полем")
    def test_error_when_creating_courier_with_empty_required_field(self, field, value):
        with allure.step("Создаём курьера с пустым полем"):
            courier = DataForCreationCourier.generate_body()
            courier[field] = value
            response = CourierMethods.created_courier(courier)
            assert response.status_code == 400