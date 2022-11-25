from flask import Flask, render_template, request

from app.roman import Roman
from app.fincalc import FinCalc

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index() -> str:
    calc = FinCalc()

    fv_pv = request.args.get('fv_pv', '')
    fv_pmt = request.args.get('fv_pmt', '')
    fv_n = request.args.get('fv_n', '')
    fv_rate = request.args.get('fv_rate', '')
    fv_freq = request.args.get('fv_freq', 'years')
    fv = {'fv_pv': fv_pv, 'fv_pmt': fv_pmt, 'fv_n': fv_n, 'fv_rate': fv_rate, 'fv_freq': fv_freq}
    print(fv)

    pmt_pv = request.args.get('pmt_pv', '')
    pmt_fv = request.args.get('pmt_fv', '')
    pmt_n = request.args.get('pmt_n', '')
    pmt_rate = request.args.get('pmt_rate', '')
    pmt_freq = request.args.get('pmt_freq', 'years')
    pmt = {'pmt_pv': pmt_pv, 'pmt_fv': pmt_fv, 'pmt_n': pmt_n, 'pmt_rate': pmt_rate, 'pmt_freq': pmt_freq}

    if fv_pv and fv_pmt and fv_n and fv_rate and fv_freq:
        if fv_freq == 'years':
            fv_val = calc.fv(float(fv_rate), int(fv_n), float(fv_pmt), float(fv_pv))
        elif fv_freq == 'months':
            fv_val = calc.fv(float(fv_rate) / 12, int(fv_n), float(fv_pmt), float(fv_pv))
        elif fv_freq == 'days':
            fv_val = calc.fv(float(fv_rate) / 252, int(fv_n), float(fv_pmt), float(fv_pv))
        print(fv_val)
    else:
        fv_val = None
    fv['val'] = fv_val

    if pmt_pv and pmt_fv and pmt_n and pmt_rate and pmt_freq:
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
