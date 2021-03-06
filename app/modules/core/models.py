from app import db
from app.modules.core import constants as USER

class User(db.Model):

    __tablename__ = 'users_user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))
    role = db.Column(db.SmallInteger, default=USER.USER)
    status = db.Column(db.SmallInteger, default=USER.NEW)

    def __init__(self, username=None, name=None, email=None, password=None):
      self.username = username
      self.name = name
      self.email = email
      self.password = password

    def getStatus(self):
      return USER.STATUS[self.status]

    def getRole(self):
      return USER.ROLE[self.role]

    def __repr__(self):
      return '<User %r>' % (self.username)

class Ticket(db.Model):

    __tablename__ = 'tickets_ticket'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    price = db.Column(db.SmallInteger)
    description = db.Column(db.String(240))
    imageurl = db.Column(db.String(120))

    def __init__(self, name=None, price=None, description=None, imageurl=None):
      self.name = name
      self.price = price
      self.description = description
      self.imageurl = imageurl

    def __repr__(self):
      return '<Ticket %r>' % (self.name)

class Equipment(db.Model):

    __tablename__ = 'equipments_equipment'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    price = db.Column(db.SmallInteger)
    description = db.Column(db.String(240))
    imageurl = db.Column(db.String(120))

    def __init__(self, name=None, price=None, description=None, imageurl=None):
      self.name = name
      self.price = price
      self.description = description
      self.imageurl = imageurl

    def __repr__(self):
      return '<Equipment %r>' % (self.name)
