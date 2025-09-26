import random
from sqlalchemy.orm import Session
from api.deps import SessionLocal
from api.services.receipts import write_receipt
from api.services.policy import load_policy, preflight_validate


def run(image_batch: dict):
    policy = load_policy("labor")
    detections = [{"sku": f"SKU-{i}", "oos": random.choice([True, False])} for i in range(3)]
    ok, sim = preflight_validate(policy, {"tasks": len(detections)})
    with SessionLocal() as db:  # type: Session
        write_receipt(
            db,
            agent="shelfvision",
            action="detect_oos",
            inputs=image_batch,
            policy_version=policy.get("version", "0.1"),
            risk_tier=policy.get("risk", "low"),
            sim_summary=sim,
            outcome={"detections": detections},
            rollback={"hint": "ignore-detections"},
        )

