from datetime import datetime, timezone
from app.db import Base
from sqlalchemy import Column, Integer, String, DateTime

class BlockedTokenModel(Base):
    __tablename__ = 'blocked-tokens'

    id = Column(Integer, primary_key=True)
    jti = Column(String(36), nullable=False)
    created_at = Column(DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))

    def __init__(self, jti: str):
        self.jti = jti
