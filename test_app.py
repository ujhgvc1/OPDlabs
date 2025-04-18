import unittest
from app import app

class TestFlaskApp(unittest.TestCase):

    # Перед каждым тестом создаём клиент
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    # Тестируем успешный POST-запрос с числами
    def test_sum(self):
        response = self.app.post('/', data={'num_1': '10', 'num_2': '20'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'30', response.data)  # Проверяем, что на странице есть число 30

    # Тестируем пустую форму (без ввода данных)
    def test_empty_form(self):
        response = self.app.post('/', data={'num_1': '', 'num_2': ''})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'0', response.data)  # Ожидаем, что будет выведена сумма 0

    # Тестируем, что приложение правильно обрабатывает некорректные данные
    def test_invalid_input(self):
        response = self.app.post('/', data={'num_1': 'abc', 'num_2': 'xyz'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'0', response.data)  # В случае ошибки ожидание будет вывод суммы как 0

if __name__ == '__main__':
    unittest.main()
