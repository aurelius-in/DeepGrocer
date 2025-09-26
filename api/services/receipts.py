import hashlib, json, os
from sqlalchemy.orm import Session
from api.models.receipt import Receipt

def _hash_inputs(payload: dict) -> str:
    return hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()

def _sign(payload: dict) -> str:
    # dev signature only; replace with HSM/KMS in prod
    key = os.getenv("SIGN_KEY","dev")
    raw = json.dumps(payload, sort_keys=True) + key
    return hashlib.sha256(raw.encode()).hexdigest()

def write_receipt(db: Session, agent: str, action: str, inputs: dict, policy_version: str, risk_tier: str, sim_summary: dict, outcome: dict, rollback: dict) -> Receipt:
    body = {
        "agent": agent, "action": action,
        "inputs_hash": _hash_inputs(inputs),
        "policy_version": policy_version,
        "risk_tier": risk_tier,
        "sim_summary": sim,
        "outcome": outcome,
        "rollback": rollback
    }
    sig = _sign(body)
    rec = Receipt(**body, signature=sig)
    db.add(rec); db.commit(); db.refresh(rec)
    return rec
