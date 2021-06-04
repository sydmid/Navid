from app.db import db 
class کارین(db.Model):
    __tablename__ = 'کارین'

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
    
    @classmethod
    def find_last_date(cls):
        result = cls.query.order_by(cls.date.desc()).first()
        return result.date


class جوین(db.Model):
    __tablename__ = 'جوین'

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
    
    @classmethod
    def find_last_date(cls):
        result = cls.query.order_by(cls.date.desc()).first()
        return result.date


class پالایش(db.Model):
    __tablename__ = 'پالایش'

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
    
    @classmethod
    def find_last_date(cls):
        result = cls.query.order_by(cls.date.desc()).first()
        return result.date


class فردا(db.Model):
    __tablename__ = 'فردا'

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
    
    @classmethod
    def find_last_date(cls):
        result = cls.query.order_by(cls.date.desc()).first()
        return result.date


class ومعادنح(db.Model):
    __tablename__ = 'ومعادنح'

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
    
    @classmethod
    def find_last_date(cls):
        result = cls.query.order_by(cls.date.desc()).first()
        return result.date


class وخارزمح(db.Model):
    __tablename__ = 'وخارزمح'

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
    
    @classmethod
    def find_last_date(cls):
        result = cls.query.order_by(cls.date.desc()).first()
        return result.date

    
    @classmethod
    def find_last_date(cls):
        result = cls.query.order_by(cls.date.desc()).first()
        return result.date


class اپال(db.Model):
    __tablename__ = 'اپال'

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
    
    @classmethod
    def find_last_date(cls):
        result = cls.query.order_by(cls.date.desc()).first()
        return result.date


class فباهنرح(db.Model):
    __tablename__ = 'فباهنرح'

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
    
    @classmethod
    def find_last_date(cls):
        result = cls.query.order_by(cls.date.desc()).first()
        return result.date


class وسهرمز(db.Model):
    __tablename__ = 'وسهرمز'

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
    
    @classmethod
    def find_last_date(cls):
        result = cls.query.order_by(cls.date.desc()).first()
        return result.date


class امینح(db.Model):
    __tablename__ = 'امینح'

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
    
    @classmethod
    def find_last_date(cls):
        result = cls.query.order_by(cls.date.desc()).first()
        return result.date


class سپیدما(db.Model):
    __tablename__ = 'سپیدما'

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
    
    @classmethod
    def find_last_date(cls):
        result = cls.query.order_by(cls.date.desc()).first()
        return result.date


class تماوندح(db.Model):
    __tablename__ = 'تماوندح'

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
    
    @classmethod
    def find_last_date(cls):
        result = cls.query.order_by(cls.date.desc()).first()
        return result.date


class خاتم(db.Model):
    __tablename__ = 'خاتم'

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
    
    @classmethod
    def find_last_date(cls):
        result = cls.query.order_by(cls.date.desc()).first()
        return result.date


class فتوسا(db.Model):
    __tablename__ = 'فتوسا'

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
    
    @classmethod
    def find_last_date(cls):
        result = cls.query.order_by(cls.date.desc()).first()
        return result.date


class زگلدشتح(db.Model):
    __tablename__ = 'زگلدشتح'

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
    
    @classmethod
    def find_last_date(cls):
        result = cls.query.order_by(cls.date.desc()).first()
        return result.date


class فگستر(db.Model):
    __tablename__ = 'فگستر'

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
    
    @classmethod
    def find_last_date(cls):
        result = cls.query.order_by(cls.date.desc()).first()
        return result.date


class سپر(db.Model):
    __tablename__ = 'سپر'

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
    
    @classmethod
    def find_last_date(cls):
        result = cls.query.order_by(cls.date.desc()).first()
        return result.date


class وبازار(db.Model):
    __tablename__ = 'وبازار'

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
    
    @classmethod
    def find_last_date(cls):
        result = cls.query.order_by(cls.date.desc()).first()
        return result.date


class باران(db.Model):
    __tablename__ = 'باران'

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
    
    @classmethod
    def find_last_date(cls):
        result = cls.query.order_by(cls.date.desc()).first()
        return result.date


class زرین(db.Model):
    __tablename__ = 'زرین'

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
    
    @classmethod
    def find_last_date(cls):
        result = cls.query.order_by(cls.date.desc()).first()
        return result.date


class خبازرس(db.Model):
    __tablename__ = 'خبازرس'

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
    
    @classmethod
    def find_last_date(cls):
        result = cls.query.order_by(cls.date.desc()).first()
        return result.date


class فراز(db.Model):
    __tablename__ = 'فراز'

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
    
    @classmethod
    def find_last_date(cls):
        result = cls.query.order_by(cls.date.desc()).first()
        return result.date


class دتوزیعح(db.Model):
    __tablename__ = 'دتوزیعح'

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
    
    @classmethod
    def find_last_date(cls):
        result = cls.query.order_by(cls.date.desc()).first()
        return result.date


class تمحرکه(db.Model):
    __tablename__ = 'تمحرکه'

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
    
    @classmethod
    def find_last_date(cls):
        result = cls.query.order_by(cls.date.desc()).first()
        return result.date


class قیستو(db.Model):
    __tablename__ = 'قیستو'

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
    
    @classmethod
    def find_last_date(cls):
        result = cls.query.order_by(cls.date.desc()).first()
        return result.date


class شستان(db.Model):
    __tablename__ = 'شستان'

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
    
    @classmethod
    def find_last_date(cls):
        result = cls.query.order_by(cls.date.desc()).first()
        return result.date

