from flask import Flask, render_template, request
from twitter2 import req
from webmap import locate


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/register', methods=["POST"])
def register():
    inp = request.form.get("domain")
    locate(req(inp))
    return render_template("map.html")


if __name__ == "__main__":
    app.run()
