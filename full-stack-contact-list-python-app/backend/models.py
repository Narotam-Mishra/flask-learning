from config import db

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(85), unique=False, nullable=False)
    last_name = db.Column(db.String(85), unique=False, nullable=False)
    email = db.Column(db.String(121), unique=True, nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email,
        }