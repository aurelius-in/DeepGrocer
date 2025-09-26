from sqlalchemy.orm import Session
from api.deps import SessionLocal
from api.services.receipts import write_receipt
from api.services.policy import load_policy, preflight_validate


def run(plan: dict):
    policy = load_policy("labor")
    qty = max(0, int(plan.get("demand", 20)))
    ok, sim = preflight_validate(policy, {"tasks": qty})
    with SessionLocal() as db:  # type: Session
        write_receipt(
            db,
            agent="mpc_replenisher",
            action="order",
            inputs=plan,
            policy_version=policy.get("version", "0.1"),
            risk_tier=policy.get("risk", "low"),
            sim_summary=sim,
            outcome={"order_qty": qty},
            rollback={"hint": "cancel-order"},
        )

