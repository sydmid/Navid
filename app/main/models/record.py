from .. import db


class Record(db.Model):
    # __tablename__ = 'stocks'

    date = db.Column(db.Date(), primary_key=True)
    open = db.Column(db.Float(precision=1))
    high = db.Column(db.Float(precision=1))
    low = db.Column(db.Float(precision=1))
    adjClose = db.Column(db.Float(precision=1))
    value = db.Column(db.Float(precision=1))
    volume = db.Column(db.Float(precision=1))
    count = db.Column(db.Float(precision=1))
    close = db.Column(db.Float(precision=1))
    # name = db.Column(db.String(80))
    # name = db.Column(db.String(80), db.ForeignKey('stocks.name'))
    # stock = db.relationship('StockModel')

    def __init__(self, **kwargs):
        self.date = kwargs['date']
        self.open = kwargs['open']
        self.high = kwargs['high']
        self.low = kwargs['low']
        self.adjClose = kwargs['adjClose']
        self.value = kwargs['value']
        self.volume = kwargs['volume']
        self.count = kwargs['count']
        self.close = kwargs['close']
        self.__tablename__ = kwargs['__tablename__']
        # self.name = kwargs['name']

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
