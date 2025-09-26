import asyncio, os
from sqlalchemy.orm import Session
from api.deps import SessionLocal
from api.services.receipts import write_receipt
from api.services.policy import load_policy, preflight_validate

POLICY_NAME="labor"  # simple bound check example

async def run_once(task_batch: dict):
    policy = load_policy(POLICY_NAME)
    ok, sim = preflight_validate(policy, {"tasks": len(task_batch.get("tasks",[]))})
    with SessionLocal() as db:  # type: Session
        rec = write_receipt(
            db, agent="task_router", action="dispatch",
            inputs=task_batch, policy_version=policy.get("version","0.1"),
            risk_tier=policy.get("risk","low"), sim_summary=sim,
            outcome={"dispatched": True, "count": len(task_batch.get("tasks",[]))},
            rollback={"hint":"reassign-tasks"}
        )
    return rec.id
