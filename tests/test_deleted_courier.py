import allure

from courier_methods import CourierMethods
from data import DataResponse
from generator import DataForCreationCourier



class TestDeletedCourier:

    @allure.title("Успешное удаление курьера")
    def test_successful_deleted_courier(self):
        with allure.step("Создаём курьера"):
            body = DataForCreationCourier.generate_body()
            CourierMethods.created_courier(body)
        with allure.step("Получаем номер id курьера"):
            login = body["login"]
            password = body["password"]
            courier_id = CourierMethods.receiving_id_courier(login, password).json()["id"]
        with allure.step("Удаляем курьера"):
            response = CourierMethods.deleted_courier(courier_id)
            response_data = response.json()
            assert response.status_code == 200 and response_data == DataResponse.TWO_HUNDRED_OK

    @allure.title("Ошибка '404' при отправки запроса с несуществующем id на удаление курьера")
    def test_error_request_without_id(self, creating_courier_and_receiving_id):
        with allure.step("Удаляем курьера"):
            response = CourierMethods.deleted_courier(1).json()
            assert response == DataResponse.FOUR_HUNDRED_FOUR_ERROR_COURIER_NOT_ID
