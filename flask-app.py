from flask import Flask, render_template, request

from app.fincalc import FinCalc

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index() -> str:
    calc = FinCalc()

    errors = {}
    fv_pv = request.args.get('fv_pv', '')
    fv_pmt = request.args.get('fv_pmt', '')
    fv_n = request.args.get('fv_n', '')
    fv_rate = request.args.get('fv_rate', '')
    fv_freq = request.args.get('fv_freq', 'years')
    fv_tax_rate = request.args.get('fv_tax_rate', 0)

    fv = calc.validate_fv_input(fv_pv, fv_pmt, fv_n, fv_rate, fv_freq, fv_tax_rate)
    print(fv)
    fv_pv, fv_pmt, fv_n, fv_rate, fv_freq, fv_tax_rate = fv['pv'], fv['pmt'], fv['n'], fv['rate'], fv['freq'], fv['tax_rate']

    if not fv['errors']:
        print('calcing fv val...')
        print(type(fv_tax_rate))
        if fv_freq == 'years':
            fv_val = calc.fv(fv_rate, fv_n, fv_pmt, fv_pv)
        elif fv_freq == 'months':
            fv_val = calc.fv(fv_rate / 12, fv_n, fv_pmt, fv_pv)
        elif fv_freq == 'days':
            fv_val = calc.fv(fv_rate / 252, fv_n, fv_pmt, fv_pv)
        pre_tax_fv = fv_val
        after_tax_fv = calc.apply_tax_rate(fv_val, fv_tax_rate)
        fv['pre_tax_val'] = pre_tax_fv
        fv['after_tax_val'] = after_tax_fv
        fv['total_tax_val'] = calc.tax_difference(pre_tax_fv, after_tax_fv)
    else:
        pass
        # pre_tax_fv = None
        # after_tax_fv = None

    print(fv['errors'])

    # fv['pre_tax_val'] = pre_tax_fv
    # fv['after_tax_val'] = after_tax_fv
    # fv['total_tax_val'] = calc.tax_difference(pre_tax_fv, after_tax_fv)
    print(fv)

    pmt_pv = request.args.get('pmt_pv', '')
    pmt_fv = request.args.get('pmt_fv', '')
    pmt_n = request.args.get('pmt_n', '')
    pmt_rate = request.args.get('pmt_rate', '')
    pmt_freq = request.args.get('pmt_freq', 'years')
    pmt_tax_rate = request.args.get('pmt_tax_rate', 0)
    pmt = calc.validate_pmt_input(pmt_pv, pmt_fv, pmt_n, pmt_rate, pmt_freq, pmt_tax_rate)
    pmt_pv, pmt_fv, pmt_n, pmt_rate, pmt_freq, pmt_tax_rate = pmt['pv'], pmt['fv'], pmt['n'], pmt['rate'], pmt['freq'], pmt['tax_rate']
    # pmt = {'pmt_pv': pmt_pv, 'pmt_fv': pmt_fv, 'pmt_n': pmt_n, 'pmt_rate': pmt_rate, 'pmt_freq': pmt_freq}

    if not pmt['errors']:
        after_tax_fv = pmt_fv / (1 - pmt_tax_rate / 100)
        print(pmt_fv, after_tax_fv)
        if pmt_freq == 'years':
            pre_tax_pmt = calc.pmt(pmt_rate, pmt_n, pmt_pv, pmt_fv)
            after_tax_pmt = calc.pmt(pmt_rate, pmt_n, pmt_pv, after_tax_fv)
        elif pmt_freq == 'months':
            pre_tax_pmt = calc.pmt(pmt_rate / 12, pmt_n, pmt_pv, pmt_fv)
            after_tax_pmt = calc.pmt(pmt_rate / 12, pmt_n, pmt_pv, after_tax_fv)
        elif pmt_freq == 'days':
            pre_tax_pmt = calc.pmt(pmt_rate / 252, pmt_n, pmt_pv, pmt_fv)
            after_tax_pmt = calc.pmt(pmt_rate / 252, pmt_n, pmt_pv, after_tax_fv)
        pmt['pre_tax_val'] = pre_tax_pmt
        pmt['after_tax_val'] = after_tax_pmt
        pmt['total_tax_val'] = calc.tax_difference(pre_tax_pmt, after_tax_pmt) * pmt_n
    else:
        pass
        # pre_tax_pmt = None
        # after_tax_pmt = None


    # pmt, fv = None, None

    # fv = {'val': fv_val}
    # pmt = {'val': pmt_val}
    print(fv)
    return render_template("index.html", fv=fv, pmt=pmt)


if __name__ == '__main__':
    app.run()
