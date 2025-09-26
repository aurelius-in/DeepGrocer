from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.deps import get_db
from api.models.receipt import Receipt

router = APIRouter()

@router.get("/receipts/latest")
def latest(db: Session = Depends(get_db), limit: int = 50):
    q = db.query(Receipt).order_by(Receipt.ts.desc()).limit(limit).all()
    return [ { "id": r.id, "ts": r.ts, "agent": r.agent, "action": r.action, "policy_version": r.policy_version, "risk_tier": r.risk_tier } for r in q ]
