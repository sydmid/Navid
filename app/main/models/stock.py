from .. import db


class StockModel(db.Model):
    __tablename__ = 'stocks'
    name = db.Column(db.String(20), primary_key=True)
    group = db.Column(db.String(20))

    def __init__(self, name):
        self.name = name

    def json(self):
        return {
                'name': self.name,
        }

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
