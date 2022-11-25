import numpy_financial as npf


class FinCalc:
    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        rep = "You've successfully instantiated a FinCalc calculator!"
        print(rep)
        return (rep)

    def fv(self, rate, n, pmt, pv, when='end'):
        if rate < 0:
            raise ValueError(
                'The rate should be a postive value. It does not make sense to invest in somethimng that pays a negative rate of return.')
        return npf.fv(rate, n, pmt, pv, when)

    def pmt(self, rate, n, pv, fv=0, when='end'):
        if rate < 0:
            raise ValueError(
                'The rate should be a postive value. It does not make sense to invest in somethimng that pays a negative rate of return.')
        return npf.pmt(rate, n, pv, fv, when)

    def rate(self, n, pmt, pv, fv, when='end'):
        return npf.rate(n, pmt, pv, fv, when)


if __name__ == '__main__':
    calc = FinCalc()
    print(calc.fv(.08, 30, -1000, 0))
    print(calc.pmt(.08, 30, 0, 100000))
    print(calc.rate(30, -1000, 0, 100000))
    print(type(calc))