from ..db import db
from datetime import datetime, timezone


class BlockedTokenModel(db.Model):
    __tablename__ = 'blocked-tokens'

    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(36), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, jti):
        self.jti = jti
        self.created_at = datetime.now(timezone.utc)

    @classmethod
    def find_by_jti(cls, jti):
        return cls.query.filter_by(jti=jti).scalar()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()



