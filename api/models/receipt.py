from sqlalchemy import Column, BigInteger, Integer, String, JSON, TIMESTAMP, text
from .base import Base

class Receipt(Base):
    __tablename__ = "receipts"
    id = Column(BigInteger, primary_key=True)
    ts = Column(TIMESTAMP, server_default=text("now()"))
    agent = Column(String, nullable=False)
    action = Column(String, nullable=False)
    inputs_hash = Column(String, nullable=False)
    policy_version = Column(String, nullable=False)
    risk_tier = Column(String, nullable=False)
    sim_summary = Column(JSON)
    outcome = Column(JSON)
    rollback = Column(JSON)
    signature = Column(String, nullable=False)
