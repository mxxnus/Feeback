from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:123456@localhost/feedback"
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ""

app.config['SQL_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# create models for the db
# (created a new table with the columns below)


class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(200), unique=True)
    source = db.Column(db.String(200))
    rating = db.Column(db.Integer)
    comments = db.Column(db.Text())

# initializer

    def __init__(self, customer, source, rating, comments):
        self.customer = customer
        self.source = source
        self.rating = rating
        self.comments = comments


# homepage
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # define data with 'name' in html form
        customer = request.form['customer']
        source = request.form['source']
        rating = request.form['rating']
        comments = request.form['comments']
        # print(customer,source,rating,comments)
        if customer == '' or source == '':
            return render_template('index.html', message='Please enter reqired fields')

        # checks whether customer already exists
        if db.session.query(Feedback).filter(Feedback.customer == customer).count() == 0:
            data = Feedback(customer, source, rating, comments)
            db.session.add(data)
            db.session.commit()

            return render_template('success.html')
        # if not true ill render the error
        return render_template('index.html', message='You have already submitted feedback')


if __name__ == '__main__':
    app.run()
