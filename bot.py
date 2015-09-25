from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")



@app.route('/settings-api')
def settingsapi():
    return render_template("settings-api.html")


@app.route('/mybots')
def mybots():
    return render_template("mybots.html")



@app.route('/mytrading')
def mytrading():
    return render_template("mytrading.html")


@app.route('/login')
def login():
    return render_template("login.html")



@app.route('/register')
def register():
    return render_template("register.html")


@app.route('/lockscreen')
def lockscreen():
    return render_template("lockscreen.html")


if __name__ == '__main__':
    app.run()
