from flask import Flask, render_template
from .models import DB, User, insert_example


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    DB.init_app(app)

    @app.route('/update')
    def update():
        # Reset the database
        DB.drop_all()
        DB.create_all()
        insert_example()
        return render_template('base.html', title='Users updated!', users=User.query.all())

    @app.route('/')
    def root():
        return render_template('base.html', title='Home', users=User.query.all())
    return app


