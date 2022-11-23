from flask import Flask, render_template, request

from app.roman import Roman

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index() -> str:
    fv_pv: str = str(request.args.get("fv_pv"))
    arabic: int = -1
    if fv_pv != "None":
        arabic = Roman.convert(fv_pv)

    return render_template("index.html", fv_pv=fv_pv, arabic=arabic)


if __name__ == '__main__':
    app.run()
