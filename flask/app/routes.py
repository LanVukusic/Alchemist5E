from app import app, db
from app.forms import LoginForm, RegistrationForm
from werkzeug.urls import url_parse
from app.models import User
from flask_login import current_user, login_user, logout_user
from flask import render_template, flash, redirect, url_for, request


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/basicguide')
def basicguide():
    return render_template('basicguide.html')


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

