from flask import Flask, render_template, request
import urllib.parse as urlparse
from urllib.parse import parse_qs

app = Flask(__name__)


@app.route('/')
def home():
    print(request.args.get("name"))
    return render_template('index.html', act_name=request.args.get("name"))


if __name__ == "__main__":
    app.run(debug=True)
