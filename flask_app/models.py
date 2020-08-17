from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()


class User(DB.Model):
    id = DB.Column(DB.BigInteger, primary_key=True)
    name = DB.Column(DB.String(15), nullable=False)

    def __str__(self):
        return f'User: {self.name}'


class Tweet(DB.Model):
    id = DB.Column(DB.BigInteger, primary_key=True)
    text = DB.Column(DB.Unicode(300))
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey('user.id'), nullable=False)
    user = DB.relationship('User', backref=DB.backref('tweets', lazy=True))

    def __str__(self):
        return f"Tweet {self.text}"


def insert_example():
    # users
    austen = User(id=1, name='austen')
    elon = User(id=2, name='elonmusk')
    nux = User(id=3, name='Nux_Taku')
    sym = User(id=4, name='Symfuhny')
    # adding to db
    DB.session.add(austen)
    DB.session.add(elon)
    DB.session.add(nux)
    DB.session.add(sym)
    # tweets
    e_tweet1 = Tweet(id=1, text='We must pass The Great Filter', user_id=2, user=elon)
    e_tweet2 = Tweet(id=2, text="Please trash me o Wikipedia I'm begging you", user_id=2, user=elon)
    nux_tweet1 = Tweet(id=3, text="When you pour a bowl of cereal then realize there's no milk", user_id=3, user=nux)
    sym_tweet1 = Tweet(id=4, text='Melted cheese ruins food...', user_id=4, user=sym)
    sym_tweet2 = Tweet(id=5, text='THIS SHOTUN IS SOOOOO BROKEN...', user_id=4, user=sym)
    a_tweet1 = Tweet(id=6, text="Something something lambda", user_id=1, user=austen)
    # adding to db
    DB.session.add(e_tweet1)
    DB.session.add(e_tweet2)
    DB.session.add(nux_tweet1)
    DB.session.add(sym_tweet1)
    DB.session.add(sym_tweet2)
    DB.session.add(a_tweet1)
    # saving changes
    DB.session.commit()
    return
