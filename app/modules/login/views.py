from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from werkzeug import check_password_hash, generate_password_hash

from app import db
from app.modules.login.forms import RegisterForm, LoginForm
from app.modules.login.decorators import requires_login
from app.modules.core.models import User


mod = Blueprint('login', __name__, url_prefix='')

@mod.before_request
def before_request():
  g.user = None
  if 'user_id' in session:
    g.user = User.query.get(session['user_id'])

@mod.route('/login/', methods=['GET', 'POST'])
def login():
  if not 'user_id' in session:
    form = LoginForm(request.form)
    # make sure data are valid, but doesn't validate password is right
    if form.validate_on_submit():
      user = User.query.filter_by(email=form.email.data).first()
      # we use werzeug to validate user's password
      if user and check_password_hash(user.password, form.password.data):
        # the session can't be modified as it's signed,
        # it's a safe place to store the user id
        session['user_id'] = user.id
        flash('Welcome %s' % user.name)
        return redirect(url_for('dashboard.home'))
      flash('Wrong email or password', 'error-message')
    return render_template("login/login.html", form=form)
  else:
    return redirect(url_for('dashboard.home'))

@mod.route('/logout/', methods=['GET'])
def logout():
  del session['user_id']
  return redirect(url_for('dashboard.home'))

@mod.route('/register/', methods=['GET', 'POST'])
def register():
  form = RegisterForm(request.form)
  if form.validate_on_submit():
    # create an user instance not yet stored in the database
    user = User(username=form.username.data, name=form.name.data, email=form.email.data, \
      password=generate_password_hash(form.password.data))
    # Insert the record in our database and commit it
    db.session.add(user)
    db.session.commit()

    # Log the user in, as he now has an id
    session['user_id'] = user.id

    # flash will display a message to the user
    flash('Thanks for registering')
    # redirect user to the 'home' method of the user module.
    return redirect(url_for('dashboard.home'))
  return render_template("login/register.html", form=form)
