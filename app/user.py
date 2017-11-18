from db_manager import db


#User database model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    # distance = db.Column(db.Integer, primary_key=True)
    school= db.Column(db.String(120), nullable = False)
    def __repr__(self):
        return '<User %r>' % self.username
