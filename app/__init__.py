import os
import sys

from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Import modules
from app.modules.dashboard.views import mod as dashboardModule
app.register_blueprint(dashboardModule)

from app.modules.login.views import mod as loginModule
app.register_blueprint(loginModule)

from app.modules.webshop.views import mod as webshopModule
app.register_blueprint(webshopModule)

from app.modules.mypage.views import mod as mypageModule
app.register_blueprint(mypageModule)

from app.modules.contact.views import mod as contactModule
app.register_blueprint(contactModule)

def add_dummydata():
    #Add dummydata
    from app.modules.core.models import User
    from app.modules.core.models import Ticket
    from app.modules.core.models import Equipment
    from werkzeug import generate_password_hash

    user = User(username='testuser', name='Testbruker Test', email='testuser@test.com', password=generate_password_hash('testtest'))

    ticket1 = Ticket(name='Dagskort', price=300, description='En hel dag med morro!', imageurl='http://placehold.it/800x300')
    ticket2 = Ticket(name='Ukeskort', price=500, description='Enda bedre, ei hel uke!', imageurl='http://placehold.it/800x300')
    ticket3 = Ticket(name='Manedskort', price=800, description='En sikker vinner', imageurl='http://placehold.it/800x300')

    equipment1 = Equipment(name='Nybegynner', price=300, description='Perfekt pakke for en nybegynner.', imageurl='http://placehold.it/800x300')
    equipment2 = Equipment(name='Medium', price=500, description='Denne pakken er litt vassere', imageurl='http://placehold.it/800x300')
    equipment3 = Equipment(name='Profesjonell', price=800, description='Topp utstyr for en ivrig skikjorer', imageurl='http://placehold.it/800x300')
    equipment4 = Equipment(name='Ekspert', price=800, description='Mye for pengene!', imageurl='http://placehold.it/800x300')
    equipment5 = Equipment(name='Toppen', price=1800, description='Det beste av det beste. En pakke for Aksel Lund Svindal.', imageurl='http://placehold.it/800x300')

    # Insert the record in our database and commit it
    db.session.add(user)
    db.session.add(ticket1)
    db.session.add(ticket2)
    db.session.add(ticket3)
    db.session.add(equipment1)
    db.session.add(equipment2)
    db.session.add(equipment3)
    db.session.add(equipment4)
    db.session.add(equipment5)
    db.session.commit()
