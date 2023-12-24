from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import date

app = Flask(__name__)


app.config.from_pyfile('config.py')

# -------for Flask SQLAlchemy we have to initialize the DB object------- #

db = SQLAlchemy(app)

# ------------------------------------------------------------------------------------------------------------------- #
# ---------------------------------------------Creating a table------------------------------------------------------ #

class Test(db.Model): # the name of the table is going to be the name of the class
    id = db.Column(db.Integer, primary_key=True)

class Member(db.Model): # the name of the table is going to be the name of the class
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(30))
    email = db.Column(db.String(50))
    join_date = db.Column(db.DateTime)

    orders = db.relationship('Order', backref='member', lazy='dynamic')

    def __repr__(self):
        return '<Member %r>' % self.username

# ---------------------------------------------Creating the table------------------------------------------------------#

# with app.app_context():
#     db.create_all()
#     print("Member table updated")

# -------------------------------------------Adding data to the table------------------------------------------------- #

# denise = Member(username='denise', password='secret', email='denise@email.com', join_date=date.today())
# michelle = Member(username='michelle', password='mypassqord', email='michelle@email.com', join_date=date.today())
# anthony = Member(username='anthony', password='123', email='anthony@email.com', join_date=date.today())
# zach = Member(username='zach', password='987654321', email='zach@email.com', join_date=date.today())

# with app.app_context():
#     db.session.add(zach)
#     db.session.commit()
# ------------------------------------------------------------------------------------------------------------------- #


# --------------------------------------------Updating data in the table--------------------------------------------- #
# with app.app_context():
#
#     anthony = Member.query.filter_by(username="anthony").first()
#
#     anthony.password = '0000'
#     db.session.commit()
#                       -------------------------
# with app.app_context():
#
#     michelle = Member.query.filter_by(username="michelle").first()
#
#     michelle.email = 'michelle@hotmail.com'
#     db.session.commit()
# ------------------------------------------------------------------------------------------------------------------- #


# -------------------------------------------------Deleting data from the table-------------------------------------- #
# with app.app_context():
    # denise = Member.query.filter_by(username='denise').first()
    # db.session.delete(denise)
    # db.session.commit()
# ------------------------------------------------------------------------------------------------------------------- #


# -----------------------------------------------------Queries------------------------------------------------------- #
# with app.app_context():
#     results = Member.query.all()
#     for r in results:
#         print(r.username)
#                                                           --*******************--

# with app.app_context():
#     ant = Member.query.filter_by(username='anthony').first()
#     print(ant.email)
#                                                           --*******************--

# with app.app_context():
#     michelle = Member.query.filter(Member.username == 'michelle').first()
#     print(michelle.password)

# with app.app_context():
#     q = Member.query
#     q = q.filter(Member.username == 'zach')
#     print(q)
#                                                           --*******************--

# with app.app_context():
#     q1 = Member.query
#     q2 = q1.filter(Member.username == 'anthony')
#     q3 = q2.filter(Member.email == 'anthony@email.com')
#     q4 = q3.filter(Member.password == 'thispassdoesntexist')
#     print(q1.all())
#     print(q2.all())
#     print(q3.all())
#     print(q4.all())
#                                                           --*******************--

#                                           -------filter for a value not equal to..-----------

# with app.app_context():
#     q = Member.query.filter(Member.username != 'anthony').all()
#     print(q)
#                                                       --*******************--

#                                           -------filter for a value like smth..-----------

# with app.app_context():
#     like_query = Member.query.filter(Member.username.like('%nth%')).all()
#     print(like_query)
#
# with app.app_context():
#     like_query = Member.query.filter(Member.username.like('%ch%')).all()
#     print(like_query)
#                                                       --*******************--

#                                             -------for member IN a list (in_)-----------
# with app.app_context():
#     q = Member.query.filter(Member.username.in_(['anthony', 'zach'])).all()
#     print(q)

# with app.app_context():
#     q = Member.query.filter(Member.username.in_(['anthony', 'zach', 'michelle'])).all()
#     print(q)
#                                       -------for member NOT IN a list(~Member...in_)-----------
# with app.app_context():
#     q = Member.query.filter(~Member.username.in_(['anthony', 'zach'])).all()
#     print(q)
#                                                        --*******************--

#                                               -------filter for a null value-----------
# with app.app_context():
#     karen = Member(username='Kar', password='karenismyname')
#     db.session.add(karen)
#     db.session.commit()

# with app.app_context():
#     q = Member.query.filter(Member.email == None).all()
#     print(q)
#                                               -------filter for a not null value-----------
# with app.app_context():
#     q = Member.query.filter(Member.email != None).all()
#     print(q)
#                                                           --*******************--

#                                               -------filter values with AND-----------
# with app.app_context():
#     q = Member.query.filter(Member.username == 'anthony').filter(Member.email == 'anthony@email.com').all()
#     print(q)
#                                                       --------or like this--------
# with app.app_context():
#     q = Member.query.filter(Member.username == 'anthony', Member.email == 'anthony@email.com').all()
#     print(q)
#                                                       --------or like this--------
# with app.app_context():
#     q = Member.query.filter(db.and_(Member.username == 'anthony', Member.email == 'anthony@email.com')).all()
#     print(q)

#                                                   -------filter values with OR-----------
# with app.app_context():
#     q1 = Member.query.filter(db.or_(Member.username == 'anthony', Member.username == 'zach')).all()
#     q2 = Member.query.filter(db.or_(Member.email == 'dghsrhrstyhs', Member.email == None)).all()
#     print(q1, q2)
#                                                           --*******************--

#                                                       -------order by-----------
# with app.app_context():
#     kar = Member.query.filter(Member.username == 'Kar').first()
#     kar.username = 'kar'
#     db.session.commit()

# with app.app_context():
#     q = Member.query.order_by(Member.username).all()
#     print(q)

# with app.app_context():
#     q = Member.query.order_by(Member.id).all()
#     print(q)
#                                                            --*******************--

#                          -                        ------limit results by using LIMIT-----------
# with app.app_context():
#     q = Member.query.limit(2).all()
#     print(q)
#
# with app.app_context():
#     q = Member.query.order_by(Member.username).limit(2).all()
#     print(q)
#                                                            --*******************--

#                                               -------offset (the opposite of LIMIT)-----------
# with app.app_context():
#     q = Member.query.offset(1).all()    #this will skip over the first result and give me all the others
#     print(q)

# with app.app_context():
#     q = Member.query.offset(2).limit(1).all()    #this will skip over the first 2 results, limit the result to 1
#     print(q)                                        #and give me all the others which wil be the 3rd result
#                                                            --*******************--

#                                                        -------count results method-----------
# with app.app_context():
#     print(Member.query.count()) # ---> 4
#     print(Member.query.filter(db.or_(Member.username == 'kar', Member.username == 'zach')).count()) # ---> 2
#                                                            --*******************--

#                                               -------inequality (greater than, less than...)-----------
# with app.app_context():
#     q = Member.query.filter(Member.id > 4).all()
#     q2 = Member.query.filter(Member.id >= 3).all()
#     print(q, q2)
#                                                            --*******************--


# ------------------------------------------------------------------------------------------------------------------- #

# ----------------------------------------------ONE TO MANY RELATIONSHIPS-------------------------------------------- #
# creating a new table that will have a connection with the Member table
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer)
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'))
#     in the Member table we also had to create another virtual column that creates the relationship in SQLAlchemy
#     orders = db.relationship('Order', backref='member', lazy='dynamic')

# with app.app_context():
#     db.create_all()
#     print('Order table created')

# with app.app_context():
#     anthony = Member.query.filter(Member.username == 'anthony').first()
#     order1 = Order(price=50, member_id=anthony.id)
#     db.session.add(order1)
#     db.session.commit()

# # ------------------------------------------------------------------------------------------------------------------- #

if __name__ == '__main__':
    app.run()
