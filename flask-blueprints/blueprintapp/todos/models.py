from blueprintapp.app import db

class Todo(db.Model):
    __tablename__ = 'todos'

    tid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    done = db.Column(db.Boolean, nullable=False)

    # this method determines how the object is represented when printed or converted to a string.
    def __repr__(self):
        return f"<TODO {self.title} Done: {self.done}>"
    
    def get_id(self):
        return self.tid