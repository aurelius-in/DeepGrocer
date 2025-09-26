from sqlalchemy.orm import Session
from api.deps import SessionLocal
from api.services.receipts import write_receipt
from api.services.policy import load_policy, preflight_validate


def run(signal: dict):
    policy = load_policy("labor")
    forecast = {"horizon": 12, "qty": max(0, int(signal.get("traffic", 50) * 0.5))}
    ok, sim = preflight_validate(policy, {"tasks": forecast["qty"]})
    with SessionLocal() as db:  # type: Session
        write_receipt(
            db,
            agent="demand_sensing",
            action="forecast",
            inputs=signal,
            policy_version=policy.get("version", "0.1"),
            risk_tier=policy.get("risk", "low"),
            sim_summary=sim,
            outcome=forecast,
            rollback={"hint": "revert-forecast"},
        )

