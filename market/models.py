from flask_login import UserMixin #Activa isAuthenticated, isAnonymous, isActive, etc..
from market import bcrypt
from market import db
from market import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    budget = db.Column(db.Float(), nullable=False, default=1500)
    items = db.relationship('Item', backref='owned_user', lazy=True)

    @property
    def password (self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        prueba = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')
        print (prueba)
        self.password_hash = prueba

    def check_password(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)

    def __repr__(self):
        return f'User: {self.username} ({self.id})'


class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Float(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self):
        return f'Item: {self.name}'


