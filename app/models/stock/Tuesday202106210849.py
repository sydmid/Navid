from app.db import db
from app.utils.stock_queries import date_functions

class غکورش(db.Model):
    __tablename__ = 'غکورش'

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
    latin_name = db.Column(db.String)
    individual_buy_power = db.Column(db.Float)
    individual_sell_power = db.Column(db.Float)
    individual_buy_sell_ratio = db.Column(db.Float)

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_record_with_date(cls, date):
        result = cls.query.get(date)
        return result

    @classmethod
    def find_last_date(cls):
        result = cls.query.order_by(cls.date.desc()).first()
        return result.date

    @classmethod
    def get_records_with_date(cls, date, mode):
        return date_functions[mode](cls, date)


class وامیدح(db.Model):
    __tablename__ = 'وامیدح'

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
    latin_name = db.Column(db.String)
    individual_buy_power = db.Column(db.Float)
    individual_sell_power = db.Column(db.Float)
    individual_buy_sell_ratio = db.Column(db.Float)

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_last_date(cls):
        result = cls.query.order_by(cls.date.desc()).first()
        return result.date

    @classmethod
    def get_records_with_date(cls, date, mode):
        return date_functions[mode](cls, date)

    @classmethod
    def get_records_with_date_api(cls, date):
        return cls.query.filter(cls.date > date).all()



