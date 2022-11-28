import requests
import unittest

class TestFinCalc(unittest.TestCase):
    url = 'https://resi-fit-quye3.ondigitalocean.app'

    def test_fincalc_returns_fincalc_object(self):
        response = requests.get(self.url)
        status_code = response.status_code
        self.assertEqual(status_code, 200)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    unittest.main(verbosity=2)
    print('Running ResiFit Unit Tests...')