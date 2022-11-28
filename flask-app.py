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

    fv = calc.validate_fv_input(fv_pv, fv_pmt, fv_n, fv_rate, fv_freq)
    print(fv)
    fv_pv, fv_pmt, fv_n, fv_rate, fv_freq = fv['pv'], fv['pmt'], fv['n'], fv['rate'], fv['freq']

    if not fv['errors']:
        print('calcing fv val...')
        if fv_freq == 'years':
            fv_val = calc.fv(fv_rate, fv_n, fv_pmt, fv_pv)
        elif fv_freq == 'months':
            fv_val = calc.fv(fv_rate / 12, fv_n, fv_pmt, fv_pv)
        elif fv_freq == 'days':
            fv_val = calc.fv(fv_rate / 252, fv_n, fv_pmt, fv_pv)
    else:
        fv_val = None

    print(fv['errors'])

    fv['val'] = fv_val
    # fv = {'fv_pv': fv_pv, 'fv_pmt': fv_pmt, 'fv_n': fv_n, 'fv_rate': fv_rate, 'fv_freq': fv_freq}
    print(fv)

    pmt_pv = request.args.get('pmt_pv', '')
    pmt_fv = request.args.get('pmt_fv', '')
    pmt_n = request.args.get('pmt_n', '')
    pmt_rate = request.args.get('pmt_rate', '')
    pmt_freq = request.args.get('pmt_freq', 'years')
    pmt = calc.validate_pmt_input(pmt_pv, pmt_fv, pmt_n, pmt_rate, pmt_freq)
    # pmt = {'pmt_pv': pmt_pv, 'pmt_fv': pmt_fv, 'pmt_n': pmt_n, 'pmt_rate': pmt_rate, 'pmt_freq': pmt_freq}

    if not pmt['errors']:
        if pmt_freq == 'years':
            pmt_val = calc.pmt(float(pmt_rate), int(pmt_n), float(pmt_pv), float(pmt_fv))
        elif pmt_freq == 'months':
            pmt_val = calc.pmt(float(pmt_rate) / 12, int(pmt_n), float(pmt_pv), float(pmt_fv))
        elif pmt_freq == 'days':
            pmt_val = calc.pmt(float(pmt_rate) / 252, int(pmt_n), float(pmt_pv), float(pmt_fv))
    else:
        pmt_val = None
    pmt['val'] = pmt_val

    # pmt, fv = None, None

    # fv = {'val': fv_val}
    # pmt = {'val': pmt_val}
    print(fv)
    return render_template("index.html", fv=fv, pmt=pmt)


if __name__ == '__main__':
    app.run()
