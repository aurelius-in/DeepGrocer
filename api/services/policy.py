import yaml, os

def load_policy(name: str) -> dict:
    root = os.getenv("POLICY_ROOT","config/policy")
    path = os.path.join(root, f"{name}.yaml")
    with open(path,"r") as f:
        return yaml.safe_load(f)

def preflight_validate(policy: dict, proposal: dict) -> tuple[bool, dict]:
    # dev: simple bounds check
    bounds = policy.get("bounds", {})
    ok = True; reasons=[]
    for k, v in bounds.items():
        if k in proposal and not (v["min"] <= proposal[k] <= v["max"]):
            ok=False; reasons.append(f"{k} out of bounds")
    return ok, {"reasons": reasons}
