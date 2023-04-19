from flask import Blueprint, render_template, request, redirect, url_for, request
from app.users.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user

blueprint = Blueprint('users', __name__)

@blueprint.get('/register')
def get_register():
    return render_template('users/register.html')

@blueprint.post('/register')
def post_register(): #add special characters etc.
    if request.form['password'] != request.form['password_confirmation']:
        return render_template('users/register.html', error='The password confirmation must match the password above')
    elif User.query.filter_by(email=request.form['email']).first():
        return render_template('users/register.html', error='The email address is already registered')
    
    user = User(
        email=request.form['email'],
        password=generate_password_hash(request.form['password'])
    )
    user.save()
    
    return redirect(url_for('users.login'))

@blueprint.get('/login')
def get_login():
    return render_template('users/login.html')

@blueprint.post('/login')
def login():
    user = User.query.filter_by(email=request.form['email']).first()

    if not user:
        return render_template('users/login.html', error='No user with the given email address was found')
    elif not check_password_hash(user.password, request.form['password']):
        return render_template('users/login.html', error='The password is not correct')

    login_user(user)
    return redirect(url_for('general_pages.index'))

    # try:
    #     user = User.query.filter_by(email=request.form.get('email')).first()

    #     if not user:
    #         raise Exception('No user with the given email address was found')
    #     elif not check_password_hash(user.password, request.form.get('password')):
    #         raise Exception('The password is not correct')
        
        # login_user(user)
        # return redirect(url_for('new_article.get_manage'))
    
    # except Exception as error_message:
    #     error = error_message or 'An error occured while logging in.'
    #     return render_template('users/login.html', error=error)

@blueprint.get('/logout')
def logout():
    logout_user()

    return redirect(url_for('general_pages.index'))