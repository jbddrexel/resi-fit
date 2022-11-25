from flask import Flask, render_template, request

from app.roman import Roman
from app.fincalc import FinCalc

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index() -> str:
    calc = FinCalc()

    fv_pv = request.args.get("fv_pv")
    fv_pmt = request.args.get("fv_pmt")
    fv_n = request.args.get("fv_n")
    fv_rate = request.args.get("fv_rate")

    pmt_pv = request.args.get("pmt_pv")
    pmt_fv = request.args.get("pmt_fv")
    pmt_n = request.args.get("pmt_n")
    pmt_rate = request.args.get("pmt_rate")

    if fv_pv and fv_pmt and fv_n and fv_rate:
        print(fv_rate, fv_n, fv_pmt, fv_pv)
        fv = calc.fv(float(fv_rate), int(fv_n), float(fv_pmt), float(fv_pv))
        print(fv)
    else:
        fv = None

    if pmt_pv and pmt_fv and pmt_n and pmt_rate:
        pmt = calc.pmt(float(pmt_rate), int(pmt_n), float(pmt_pv), float(pmt_fv))
    else:
        pmt = None

    # pmt, fv = None, None

    return render_template("index.html", fv=fv, pmt=pmt)


if __name__ == '__main__':
    app.run()
