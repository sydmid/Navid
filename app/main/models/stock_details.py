from .. import db


class StockDetails(db.Model):
    __tablename__ = 'stock-table'
    # date,open,high,low,adjClose,value,volume,count,close
    date = db.Column(db.Date(), primary_key=True)
    name = db.Column(db.String(80))
    open = db.Column(db.Float(precision=1))
    high = db.Column(db.Float(precision=1))
    low = db.Column(db.Float(precision=1))
    adjClose = db.Column(db.Float(precision=1))
    value = db.Column(db.Float(precision=1))
    volume = db.Column(db.Float(precision=1))
    count = db.Column(db.Float(precision=1))
    close = db.Column(db.Float(precision=1))
    stock_id = db.Column(db.Integer, db.ForeignKey('stocks.id'))
    stock = db.relationship('StockModel')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'id': self.id, 'name': self.name, 'price': self.price, 'store_id': self.store_id}

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
