from market import db, bcrypt, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=15), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=1000)
    items = db.relationship('Item', backref='owned_user', lazy=True)

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_txt_pw):
        self.password_hash = bcrypt.generate_password_hash(plain_txt_pw).decode('utf-8')
    
    @property
    def budget_display(self):
        return f'{self.budget:,}$'

    def can_purchase(self, item_to_purchase):
        return self.budget >= item_to_purchase.price
    
    def can_sell(self, item_to_sell):
        return item_to_sell in self.items


class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def assign_buyer(self, buyer):
        self.owner = buyer.id
        buyer.budget -= self.price
        db.session.commit()

    def sell_item(self, seller):
        self.owner = None
        seller.budget += self.price
        db.session.commit()

    def __repr__(self):
        return f'Item {self.name}'
