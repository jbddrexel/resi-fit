import numpy_financial as npf


class FinCalc:
    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        rep = "You've successfully instantiated a FinCalc calculator!"
        print(rep)
        return rep

    def validate_fv_input(self, pv, pmt, n, rate, freq):
        values = {
            'pv': pv,
            'pmt': pmt,
            'n': n,
            'rate': rate,
            'freq': freq,
            'errors': {}
        }
        if not pv or pv == '0.0':
            pv, values['pv'] = 0, 0
        if not pmt or pmt == '0.0':
            pmt, values['pmt'] = 0, 0
        if (pv or pmt) and n and rate and freq:
            values = self.validate_input(values)
        else:
            values['errors']['param_count'] = 'When using the future value calculator, you must supply values for the number of periods, ' \
                               'rate, frequency and starting balance and/or contribution.'
        return values

    def validate_pmt_input(self, pv, fv, n, rate, freq):
        values = {
            'pv': pv,
            'fv': fv,
            'n': n,
            'rate': rate,
            'freq': freq,
            'errors': {}
        }
        if not pv or pv == '0.0':
            pv, values['pv'] = 0, 0
        if not fv or fv == '0.0':
            fv, values['fv'] = 0, 0
        if (pv or fv) and n and rate and freq:
            values = self.validate_input(values)
        else:
            values['errors']['param_count'] = 'When using the payment calculator, you must supply values for the number of periods, ' \
                               'rate, frequency and starting balance and/or ending balance.'
        return values
    def validate_input(self, params):
        values = params.copy()
        values['errors'] = {}
        for param, value in params.items():
            if param in ('fv', 'pv', 'pmt', 'rate',):
                try:
                    values[param] = float(value)
                except ValueError as e:
                    values['errors'][param] = f'{value} is not a valid input. Try inputting a number.'
                else:
                    if param == 'rate' and values[param] <= 0:
                        values['errors'][param] = f'Try inputting a rate greater than zero. Investing at rates <= 0 is not a sound investment plan!'
            elif param == 'freq':
                if value not in ('years', 'months', 'days'):
                    values['errors'][param] = f'Please use a payment frequency of either years, months or days.'
            elif param == 'n':
                try:
                    values[param] = int(value)
                except ValueError as e:
                    values['errors'][param] = f'{value} is not a valid Number of Periods. Try inputting a whole number.'
                else:
                    if values[param] <= 0:
                        values['errors'][param] = f'Number of periods must be a whole number greater than zero!'
        return values

    def fv(self, rate=0, n=0, pmt=0, pv=0, when='end'):
        rate = rate / 100
        return npf.fv(rate, n, pmt, pv, when)

    def pmt(self, rate, n, pv=0, fv=0, when='end'):
        rate = rate / 100
        return npf.pmt(rate, n, pv, fv, when)

    def rate(self, n, pmt, pv, fv, when='end'):
        return npf.rate(n, pmt, pv, fv, when) * 100


if __name__ == '__main__':
    calc = FinCalc()
    print(calc.fv(.08, 30, -1000, 0))
    print(calc.pmt(.08, 30, 0, 100000))
    print(calc.rate(30, -1000, 0, 100000))
    print(type(calc))