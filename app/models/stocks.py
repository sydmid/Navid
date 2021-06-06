from app.db import db

class Stocks(db.Model):
    __bind_key__ = 'stocks_dict'
    __tablename__ = 'stocks_page'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15))
    group = db.Column(db.String(30))
    url = db.Column(db.String)
    open = db.Column(db.Float)
    high = db.Column(db.Float)
    low = db.Column(db.Float)
    adjClose = db.Column(db.Float)
    value = db.Column(db.Integer)
    volume = db.Column(db.Integer)
    count = db.Column(db.Integer)
    close = db.Column(db.Float)
    individual_buy_count = db.Column(db.Integer)
    individual_sell_count = db.Column(db.Integer)
    individual_buy_vol = db.Column(db.Integer)
    individual_sell_vol = db.Column(db.Integer)
    individual_buy_value = db.Column(db.Integer)
    individual_sell_value = db.Column(db.Integer)
    corporate_buy_count = db.Column(db.Integer)
    corporate_sell_count = db.Column(db.Integer)
    corporate_buy_vol = db.Column(db.Integer)
    corporate_sell_vol = db.Column(db.Integer)
    corporate_buy_value = db.Column(db.Integer)
    corporate_sell_value = db.Column(db.Integer)
    individual_buy_mean_price = db.Column(db.Float)
    individual_sell_mean_price = db.Column(db.Float)
    corporate_buy_mean_price = db.Column(db.Float)
    corporate_sell_mean_price = db.Column(db.Float)
    individual_ownership_change = db.Column(db.Integer)


    @classmethod
    def query_all_names(cls):
        return cls.query.all()