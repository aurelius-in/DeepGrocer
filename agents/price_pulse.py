from sqlalchemy.orm import Session
from api.deps import SessionLocal
from api.services.receipts import write_receipt
from api.services.policy import load_policy, preflight_validate


def run(signal: dict):
    policy = load_policy("pricing")
    elasticity = float(signal.get("elasticity", -1.2))
    markdown_pct = min(30, max(0, int(abs(elasticity) * 10)))
    ok, sim = preflight_validate(policy, {"markdown_pct": markdown_pct})
    with SessionLocal() as db:  # type: Session
        write_receipt(
            db,
            agent="price_pulse",
            action="price_adjust",
            inputs=signal,
            policy_version=policy.get("version", "0.1"),
            risk_tier=policy.get("risk", "low"),
            sim_summary=sim,
            outcome={"markdown_pct": markdown_pct},
            rollback={"hint": "revert-price"},
        )

