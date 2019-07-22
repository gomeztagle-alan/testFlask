from flask import Flask, render_template, request, redirect, url_for
from models import db, User
from forms import UsersForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/usersdb'
db.init_app(app)

app.secret_key = "e14a-key"

@app.route("/")
@app.route("/index")
def index():
  return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():

    form = UsersForm()
    if request.method == 'GET':
        return render_template('login.html', form=form)
    else:
        return render_template("dashboard.html")

@app.route('/dashboard')
def  dashboard():
    return render_template('dashboard.html')

if __name__ == "__main__":
  app.run(debug=True)
