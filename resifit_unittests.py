import unittest
from FinCalc import FinCalc

class TestFinCalc(unittest.TestCase):
    calc = FinCalc()

    def test_fincalc_returns_fincalc_object(self):
        self.assertEqual(type(self.calc), FinCalc)
    
    def test_fincacl_str_method(self):
        self.assertEqual(self.calc.__str__(), "You've successfully instantiated a FinCalc calculator!")

    def test_fv_1(self):
        fv = round(self.calc.fv(.08, 30, -1000, 0), 2)
        self.assertEqual(fv, 113283.21)

    def test_fv_2(self):
        self.assertRaises(ValueError, self.calc.fv, -.08, 30, -1000, 0)
        
    def test_pmt_1(self):
        pmt = round(self.calc.pmt(.08, 30, 0, 100000), 2)
        self.assertEqual(pmt, -882.74)

    def test_pmt_2(self):
        self.assertRaises(ValueError, self.calc.pmt, -.08, 30, -1000, 0)

    def test_rate_1(self):
        rate = round(self.calc.rate(30, -1000, 0, 100000), 4)
        self.assertEqual(rate, .0732)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    unittest.main(verbosity=2)
    print('Running ResiFit Unit Tests...')
    