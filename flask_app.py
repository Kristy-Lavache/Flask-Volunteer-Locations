
# A very simple Flask Hello World app for you to get started with...

from flask import render_template

app = Flask(__name__)

@app.route('/', methods=["Get"])
def index():
    return render_template("main_page.html")

