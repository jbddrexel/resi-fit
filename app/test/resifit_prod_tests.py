import requests
import unittest

class ProdTests(unittest.TestCase):
    url = 'https://resi-fit-quye3.ondigitalocean.app'

    def test_server_is_up_and_running(self):
        response = requests.get(self.url)
        status_code = response.status_code
        self.assertEqual(status_code, 200)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    unittest.main(verbosity=2)
    print('Running ResiFit Unit Tests...')