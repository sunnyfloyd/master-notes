from market import app, db
from flask import render_template, redirect, url_for, flash, request
from market.models import Item, User
from market.forms import RegisterForm, LoginForm, PurchaseItemForm, SellItemForm
from flask_login import login_user, current_user, login_required, logout_user


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market', methods=['GET', 'POST'])
@login_required
def market_page():
    purchase_form = PurchaseItemForm()
    sell_form = SellItemForm()
    if request.method == 'POST':
        # Purchase item logic
        if purchase_form.validate_on_submit():
            purchased_item = request.form.get('purchased_item')
            p_item_object = Item.query.filter_by(name=purchased_item).first()
            if p_item_object:
                if current_user.can_purchase(p_item_object):
                    p_item_object.assign_buyer(current_user)
                    flash(f'You purchased {p_item_object.name} for {p_item_object.price}', category='info')
                else:
                    flash(f'You do not have sufficient funds on your account!', category='danger')
        # Sell item logic
        if sell_form.validate_on_submit():
            p_item_object = Item.query.filter_by(name=request.form.get('sold_item')).first()
            if p_item_object:
                if current_user.can_sell(p_item_object):
                    p_item_object.sell_item(current_user)
                    flash('Item has been successfully sold!', category='info')
                else:
                    flash('You do not own this item!!', category='danger')
        return redirect(url_for('market_page'))
        
    if request.method == 'GET':
        items = Item.query.filter_by(owner=None)
        user_items = Item.query.filter_by(owner=current_user.id)
    return render_template('market.html', items=items, user_items=user_items, purchase_form=purchase_form, sell_form=sell_form)

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    if current_user.is_authenticated:
        flash('You are already logged in!', 'success')
        return redirect(url_for('home_page'))
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(
            username=form.username.data,
            email_address=form.email_address.data,
            password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        
        login_user(user_to_create)
        flash(  'User has been created successfully! You are now logged in to the page.',
                category='info')
        return redirect(url_for('market_page'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(
                f'Following error occured when trying to create the user: {err_msg}',
                category='danger')
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if current_user.is_authenticated:
        flash('You are already logged in!', 'success')
        return redirect(url_for('home_page'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        login_user(user)
        flash(f'You have successfully logged in as {user.username}', category='success')
        return redirect(url_for('market_page'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(
                f'Following error occured when trying to login: {err_msg}',
                category='danger')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout_page():
    logout_user()
    flash('You have been logged out.', category='info')
    return redirect(url_for('home_page'))
