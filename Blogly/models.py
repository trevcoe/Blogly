from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE_URL = "https://icon-library.com/icon/default-user-icon-26.html.html>Default User Icon # 21965"

class User(db.model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_ley = True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE_URL)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

def connect_db(app):
    """connecting this database to provided Flask app"""
    db.app = app
    db.init_app(app)