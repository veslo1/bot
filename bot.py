from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")



@app.route('/settings')
def settings():
    return render_template("settings.html")


@app.route('/mybots')
def mybots():
    return render_template("mybots.html")


if __name__ == '__main__':
    app.run()
