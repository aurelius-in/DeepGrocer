from fastapi import APIRouter
router = APIRouter()

@router.post("/agents/run/{name}")
def run_agent(name: str):
    return {"queued": name}
