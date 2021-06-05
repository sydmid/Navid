from app.db import db
from sqlalchemy import cast, String

class خودرو(db.Model):
    __tablename__ = 'خودرو'

    name = db.Column(db.String(15))
    group = db.Column(db.String(30))
    date = db.Column(db.Date, primary_key=True)
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
    jdate = db.Column(db.String)

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def stock_from_date(cls, date, mode):
        lambda_functions = {
            'chart-full': lambda x: x.query.filter(x.date > date).with_entities(x.date.cast(String), x.open, x.adjClose,
                                                                                x.volume).all(),
            'general-all': lambda x: x.query.filter(x.date > date).with_entities(x.date.cast(String), x.open, x.adjClose,
                                                                                 x.volume, x.high, x.low, x.count,
                                                                                 x.value, x.close).all(),
            'clients-all': lambda x: x.query.filter(x.date > date).with_entities(x.date.cast(String),
                                                                                 x.individual_buy_count,
                                                                                 x.individual_sell_count,
                                                                                 x.individual_buy_vol,
                                                                                 x.individual_sell_vol,
                                                                                 x.individual_buy_value,
                                                                                 x.individual_sell_value,
                                                                                 x.corporate_buy_count,
                                                                                 x.corporate_sell_count,
                                                                                 x.corporate_buy_vol ,
                                                                                 x.corporate_sell_vol,
                                                                                 x.corporate_buy_value,
                                                                                 x.corporate_sell_value,
                                                                                 x.individual_buy_mean_price,
                                                                                 x.individual_sell_mean_price,
                                                                                 x.corporate_buy_mean_price,
                                                                                 x.corporate_sell_mean_price,
                                                                                 x.individual_ownership_change,).all(),
            'all': lambda x: x.query.filter(x.date > date).with_entities(x.date.cast(String),
                                                                         x.open, x.adjClose,
                                                                         x.volume, x.high, x.low, x.count,
                                                                         x.value, x.close,
                                                                         x.individual_buy_count,
                                                                         x.individual_sell_count,
                                                                         x.individual_buy_vol,
                                                                         x.individual_sell_vol,
                                                                         x.individual_buy_value,
                                                                         x.individual_sell_value,
                                                                         x.corporate_buy_count,
                                                                         x.corporate_sell_count,
                                                                         x.corporate_buy_vol ,
                                                                         x.corporate_sell_vol,
                                                                         x.corporate_buy_value,
                                                                         x.corporate_sell_value,
                                                                         x.individual_buy_mean_price,
                                                                         x.individual_sell_mean_price,
                                                                         x.corporate_buy_mean_price,
                                                                         x.corporate_sell_mean_price,
                                                                         x.individual_ownership_change,).all(),
        }
        return lambda_functions[mode](cls)
