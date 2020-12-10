from flask import Flask, render_template, request
import urllib.parse as urlparse
from urllib.parse import parse_qs

app = Flask(__name__)


@app.route('/')
def home():
    # print(request.args.get("name"))
    return render_template('index3.html', showSuccessMsg="")


@app.route('/thank-you')
def thankyou():
    # print(request.args.get("name"))
    return render_template('index3.html', showSuccessMsg="Thank you for Registering!")


if __name__ == "__main__":
    app.run(debug=True)
