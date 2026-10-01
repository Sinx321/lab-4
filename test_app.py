import unittest
from app import app, calculate_volume


class TestVolumeApp(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_main_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Калькулятор объёма', response.data)
        print(" Тест 1 пройден")

    def test_cube_volume_calculation(self):
        response = self.client.post('/', data={
            'figure': 'cube',
            'param': '5'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'125.00', response.data)
        print(" Тест 2 пройден")

    def test_negative_number_error(self):
        response = self.client.post('/', data={
            'figure': 'cube',
            'param': '-3'
        })
        self.assertIn(b'не может быть отрицательным', response.data)
        print("  Тест 3 пройден")

    def test_invalid_input_error(self):
        response = self.client.post('/', data={
            'figure': 'cube',
            'param': 'abc'
        })
        self.assertIn(b'корректное число', response.data)
        print(" Тест 4 пройден")


if __name__ == '__main__':
    unittest.main()