from sqlalchemy.orm import Session
from api.deps import SessionLocal
from api.services.receipts import write_receipt
from api.services.policy import load_policy, preflight_validate

def run_prediction(signal: dict) -> dict:
    traffic = signal.get("traffic", 0)
    open_lanes = 1 if traffic > 80 else 0
    return {"open_lanes": open_lanes, "traffic": traffic}

def run(signal: dict):
    policy = load_policy("labor")
    outcome = run_prediction(signal)
    ok, sim = preflight_validate(policy, {"open_lanes": outcome["open_lanes"]})
    with SessionLocal() as db:
        write_receipt(
            db, agent="queueflow", action="lane_adjust",
            inputs=signal, policy_version=policy.get("version","0.1"),
            risk_tier=policy.get("risk","low"), sim_summary=sim,
            outcome=outcome, rollback={"hint":"close-lane"}
        )
