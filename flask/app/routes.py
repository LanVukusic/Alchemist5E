from app import app, db
from app.forms import LoginForm, RegistrationForm
from werkzeug.urls import url_parse
from app.models import User
from flask_login import current_user, login_user, logout_user, login_required
from flask import render_template, flash, redirect, url_for, request, jsonify

values = [
      {
        "name": 'Elixir of Conflicts',
        "cost": 820
      },
      {
        "name": 'Philter of Dream Inducement',
        "cost": 120
      },
      {
        "name": 'Elixir of Enhanced Sleep',
        "cost": 510
      },
      {
        "name": 'Elixir of Enhanced Sleep',
        "cost": 20
      },
      {
        "name": 'Flask of the Oracle',
        "cost": 1337
      },
      {
        "name": 'Phial of Pain',
        "cost": 30
      },
      {
        "name": 'Brew of Hysteria',
        "cost": 50
      },
      {
        "name": 'Flask of Endless Time',
        "cost": 10
      }
    ]


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home', potions=values)


@app.route('/basicguide')
def basicguide():
    return render_template('basicguide.html')


@app.route('/herbeditor')
@login_required
def herbeditor():
    return render_template('herbeditor.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/login', methods=['GET', 'POST'])  # Default method is only get, so we need to over-ride it.
def login():

    if current_user.is_authenticated:  # If the user is already logged in:
        return redirect(url_for('index'))  # Redirect him back to main page as that was probably a mistake.

    form = LoginForm()  # Creating a new form object inherited from app/forms.py

    if form.validate_on_submit():  # Is called when a get or post method is returned. Will be false on get.
        c_user = User.query.filter_by(username=form.username.data).first()  # Load the user from database.
        # We are only expecting one result so we are calling first, getting the User or else None.

        if c_user is None or not c_user.check_password(form.password.data):  # Self explanatory.
            flash('Invalid username or password')
            return redirect(url_for('login'))

        login_user(c_user, remember=form.remember_me.data)  # Register user as logged in.
        # Future pages navigated will have "current_user" assigned to this user.

        # Because the login page can be called from any page on the website, we must redirect the user to the page from
        # where the login was called, so we return them to the desired site.
        next_page = request.args.get('next')  # We parse the data from the url, which should have a "next" argument.
        if not next_page or url_parse(next_page).netloc != '':  # For security reasons we check if the url is relative!
            next_page = url_for('index')

        return redirect(next_page)

    return render_template('login.html', title='Sign In', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegistrationForm()

    if form.validate_on_submit():
        c_user = User(username=form.username.data, email=form.email.data)
        c_user.set_password(form.password.data)
        db.session.add(c_user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form=form)


@app.route('/_get_list_data', methods=['POST'])
def get_list_data():
    if request.method == 'POST':
        a = request.get_json()
        if a.get('a') == 1:
            return jsonify(result=values)
        else:
            return jsonify("Bad request")


