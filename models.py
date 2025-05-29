from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String, nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Rating image_url={self.image_url} rating={self.rating}>'
