import os

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///web.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Register(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(300), nullable=False)
    full_name = db.Column(db.String(300), nullable=False)

    def __repr__(self):  # Исправлено на __repr__
        return self.id


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form['email']
        full_name = request.form['full_name']

        reg = Register(email=email, full_name=full_name)

        try:
            db.session.add(reg)
            db.session.commit()
            # return redirect('/')
        except:
            return 'Произошла ошибка при добавлении вопроса'
    return render_template('index.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5000)