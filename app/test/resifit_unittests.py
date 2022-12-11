import unittest
from app.fincalc import FinCalc


class TestFinCalc(unittest.TestCase):
    calc = FinCalc()

    def test_fincalc_returns_fincalc_object(self):
        self.assertEqual(type(self.calc), FinCalc)

    def test_fincacl_str_method(self):
        self.assertEqual(self.calc.__str__(), "You've successfully instantiated a FinCalc calculator!")

    def test_fv_1(self):
        fv = round(self.calc.fv(8, 30, -1000, 0), 2)
        self.assertEqual(fv, 113283.21)

    def test_pmt_1(self):
        pmt = round(self.calc.pmt(8, 30, 0, 100000), 2)
        self.assertEqual(pmt, -882.74)

    def test_rate_1(self):
        rate = round(self.calc.rate(30, -1000, 0, 100000), 4)
        self.assertEqual(rate, 7.3157)

    # make sure values['errors'] is empty
    def test_good_inputs_1(self):
        params = {
            'pv': -100000,
            'pmt': -1000,
            'fv': 0,
            'n': 30,
            'rate': 8.25,
            'freq': 'years'
        }
        values = self.calc.validate_input(params)
        self.assertEqual(values['errors'], {})

    # make sure the values returned are the same as those input with also an entry for 'errors'
    # that will be blank
    def test_good_inputs_2(self):
        params = {
            'pv': -100000,
            'pmt': -1000,
            'fv': 0,
            'n': 30,
            'rate': 8.25,
            'freq': 'years'
        }
        values = self.calc.validate_input(params)
        params['errors'] = {}
        self.assertEqual(values, params)

    # pass some good inputs that happen to be strings. validate_input should be able to convert them.
    def test_good_inputs_str_type(self):
        params = {
            'pv': '-100000',
            'pmt': -1000,
            'fv': '0',
            'n': 30,
            'rate': 8.25,
            'freq': 'years'
        }
        values = self.calc.validate_input(params)
        expected_params = {
            'pv': -100000,
            'pmt': -1000,
            'fv': 0,
            'n': 30,
            'rate': 8.25,
            'freq': 'years',
            'errors': {}
        }
        self.assertEqual(values, expected_params)

    def test_only_one_param(self):
        params = {
            'pv': -100000
        }
        values = self.calc.validate_input(params)
        self.assertEqual(values['errors'], {})

    def test_one_bad_param_one_good_one(self):
        params = {
            'pv': -100000,
            'rate': -12
        }
        values = self.calc.validate_input(params)
        self.assertEqual(values['errors']['rate'], 'Try inputting a rate greater than zero. Investing at rates <= 0 is not a sound investment plan!')

    def test_bad_pv(self):
        params = {
            'pv': 'asdf',
            'pmt': -1000,
            'fv': 0,
            'n': 30,
            'rate': -12,
            'freq': 'years'
        }
        values = self.calc.validate_input(params)
        self.assertEqual(values['errors']['pv'],
                         f'asdf is not a valid input. Try inputting a number.')

    def test_bad_fv(self):
        params = {
            'pv': -100000,
            'pmt': -1000,
            'fv': 'self',
            'n': 30,
            'rate': -12,
            'freq': 'years'
        }
        values = self.calc.validate_input(params)
        self.assertEqual(values['errors']['fv'],
                         f'self is not a valid input. Try inputting a number.')
    def test_bad_pmt(self):
        params = {
            'pv': -100000,
            'pmt': 'foo',
            'fv': 0,
            'n': 30,
            'rate': -12,
            'freq': 'years'
        }
        values = self.calc.validate_input(params)
        self.assertEqual(values['errors']['pmt'],
                         f'foo is not a valid input. Try inputting a number.')
    def test_bad_n(self):
        params = {
            'pv': -100000,
            'pmt': -1000,
            'fv': 0,
            'n': 'bar',
            'rate': -12,
            'freq': 'years'
        }
        values = self.calc.validate_input(params)
        self.assertEqual(values['errors']['n'],
                         f'bar is not a valid Number of Periods. Try inputting a whole number.')
    def test_bad_freq(self):
        params = {
            'pv': -100000,
            'pmt': -1000,
            'fv': 0,
            'n': 30,
            'rate': 12,
            'freq': 'hey hey!'
        }
        values = self.calc.validate_input(params)
        self.assertIn(values['errors']['freq'],
                         f'Please use a payment frequency of either years, months or days.')

    def test_bad_rate(self):
        params = {
            'pv': -100000,
            'pmt': -1000,
            'fv': 0,
            'n': 30,
            'rate': 'this is great',
            'freq': 'years'
        }
        values = self.calc.validate_input(params)
        self.assertEqual(values['errors']['rate'],
                         f'this is great is not a valid input. Try inputting a number.')

    def test_negative_rate(self):
        params = {
            'pv': -100000,
            'pmt': -1000,
            'fv': 0,
            'n': 30,
            'rate': -12,
            'freq': 'years'
        }
        values = self.calc.validate_input(params)
        self.assertEqual(values['errors']['rate'],
                         'Try inputting a rate greater than zero. Investing at rates <= 0 is not a sound investment plan!')

    def test_negative_n(self):
        params = {
            'pv': -100000,
            'pmt': -1000,
            'fv': 0,
            'n': -30,
            'rate': 12,
            'freq': 'years'
        }
        values = self.calc.validate_input(params)
        self.assertEqual(values['errors']['n'],
                         f'Number of periods must be a whole number greater than zero!')

    def test_validate_fv_input_missing_params(self):
        values = self.calc.validate_fv_input(0, 0, 10, 8, 'years')
        self.assertEqual(values['errors']['param_count'], 'When using the future value calculator, you must supply values for the number of periods, ' \
                               'rate, frequency and starting balance and/or contribution.')

    def test_validate_pmt_input_missing_params(self):
        values = self.calc.validate_pmt_input(0, 0, 10, 8, 'years')
        self.assertEqual(values['errors']['param_count'], 'When using the payment calculator, you must supply values for the number of periods, ' \
                               'rate, frequency and starting balance and/or ending balance.')

    def test_apply_tax_rate_1(self):
        bal = self.calc.apply_tax_rate(100, 30)
        self.assertEqual(bal, 70)

    def test_apply_tax_rate_2(self):
        bal = self.calc.apply_tax_rate(100, 70)
        self.assertEqual(int(bal), 30)

    def test_invert_tax_rate_1(self):
        bal = round(self.calc.invert_tax_rate(100, 30), 2)
        self.assertEqual(bal, 142.86)

    def test_invert_tax_rate_2(self):
        bal = round(self.calc.invert_tax_rate(100, 70), 2)
        self.assertEqual(bal, 333.33)

    def test_bad_tax_rate_pmt_calc(self):
        values = self.calc.validate_pmt_input(-100, 1000, 10, 8, 'years', -70)
        self.assertEqual(values['errors']['tax_rate'],
                         f'Try inputting a tax rate greater than or equal to zero.')
    def test_bad_tax_rate_pv_calc(self):
        values = self.calc.validate_fv_input(-100, -100, 10, 8, 'years', -70)
        self.assertEqual(values['errors']['tax_rate'],
                         f'Try inputting a tax rate greater than or equal to zero.')

    def test_good_tax_rate(self):
        params = {
            'tax_rate': 20
        }
        values = self.calc.validate_input(params)
        self.assertEqual(values['errors'], {})

    def test_bad_tax_rate_validate_input_1(self):
        params = {
            'pv': -100000,
            'pmt': -1000,
            'fv': 0,
            'n': 30,
            'rate': 8,
            'freq': 'years',
            'tax_rate': 'great!'
        }
        values = self.calc.validate_input(params)
        self.assertEqual(values['errors']['tax_rate'],
                         f'great! is not a valid input. Try inputting a number.')

    def test_bad_tax_rate_validate_input_2(self):
        params = {
            'pv': -100000,
            'pmt': -1000,
            'fv': 0,
            'n': 30,
            'rate': 8,
            'freq': 'years',
            'tax_rate': -30
        }
        values = self.calc.validate_input(params)
        self.assertEqual(values['errors']['tax_rate'],
                         f'Try inputting a tax rate greater than or equal to zero.')

    def test_bad_tax_rate_only_1(self):
        params = {
            'tax_rate': -30
        }
        values = self.calc.validate_input(params)
        self.assertEqual(values['errors']['tax_rate'],
                         f'Try inputting a tax rate greater than or equal to zero.')

    def test_bad_tax_rate_only_2(self):
        params = {
            'tax_rate': 'bad rate!'
        }
        values = self.calc.validate_input(params)
        self.assertEqual(values['errors']['tax_rate'],
                         f'bad rate! is not a valid input. Try inputting a number.')

    def test_tax_difference(self):
        diff = self.calc.tax_difference(100000, 70000)
        self.assertEqual(diff, 30000)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    unittest.main(verbosity=2)
    print('Running ResiFit Unit Tests...')