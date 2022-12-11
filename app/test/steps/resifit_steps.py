from behave import *
from app.fincalc import FinCalc

# use_step_matcher("re")

calc = FinCalc()
params = {
    'pv': -100000,
    'pmt': -1000,
    'n': 30,
    'rate': 8
}
# ARBITRARY_MESSAGE = "Hello, world"

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
#
# @given('Lucy is at {xCoord:d}, {yCoord:d}')
# def step_impl(context, xCoord, yCoord):
#     SHOUTY.set_location("Lucy", Coordinate(xCoord, yCoord))
#
#
# @step('Sean is at {xCoord:d}, {yCoord:d}')
# def step_impl(context, xCoord, yCoord):
#     SHOUTY.set_location("Sean", Coordinate(xCoord, yCoord))
#
#
# @when('Sean shouts')
# def step_impl(context):
#     SHOUTY.shout("Sean", ARBITRARY_MESSAGE)
#
#
# @then('Lucy should hear Sean')
# def step_impl(context):
#     assert(1 == len(SHOUTY.get_shouts_heard_by("Lucy")))
#
#
# @then('Lucy should hear nothing')
# def step_impl(context):
#     assert(0 == len(SHOUTY.get_shouts_heard_by("Lucy")))
