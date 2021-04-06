from .. import db


class StockModel(db.Model):
    __tablename__ = 'stocks'

    name = db.Column(db.String(80), primary_key=True)
    group = db.Column(db.String(80))
    # records = db.relationship('Record', lazy='dynamic')
    # group_id = db.Column(db.Integer, db.ForeignKey('groups.id'))
    # stock = db.relationship('GroupModel')

    def __init__(self, name):
        self.name = name

    def json(self):
        return {'id': self.id,
                'name': self.name,
                'items': [item.json() for item in self.items.all()]}

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
