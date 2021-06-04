from app.db import db


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
    def find_by_time_ago(cls, _time):
        result = cls.query.filter(cls.date > _time).first()
        return result

    @classmethod
    def find_last_date(cls):
        result = cls.query.order_by(cls.date.desc()).first()
        return result.date

    def json_payload(self):
        return {'info': 'its ok man'}, 200
