from behave import *
from app.fincalc import FinCalc

calc = FinCalc()
params = {
    'pv': -100000,
    'pmt': -1000,
    'n': 30,
    'rate': 8
}

@given('a financial calculator')
def step_impl(context):
    isinstance(calc, FinCalc)

@step('some correct input parameters')
def step_impl(context):
    calc.validate_input(params)

@when('we use the calculator')
def step_impl(context):
    pv, pmt, n, rate = params['pv'], params['pmt'], params['n'], params['rate']
    calc.fv(rate, n, pmt, pv)

@then('we should receive a calculated investment balance')
def step_impl(context):
    pv, pmt, n, rate = params['pv'], params['pmt'], params['n'], params['rate']
    bal = round(calc.fv(rate, n, pmt, pv), 2)
    assert bal == 1119548.90
