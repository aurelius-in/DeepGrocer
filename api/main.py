from fastapi import FastAPI, Response
from api.routers import health, receipts, agents
from prometheus_client import Counter, generate_latest

app = FastAPI(title="DeepGrocer API")

REQS = Counter("dg_api_requests_total","Total API requests")

@app.middleware("http")
async def count_requests(request, call_next):
    response = await call_next(request)
    REQS.inc()
    return response

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")

app.include_router(health.router, tags=["health"])
app.include_router(receipts.router, prefix="/api", tags=["receipts"])
app.include_router(agents.router, prefix="/api", tags=["agents"])

@app.get("/")
def root():
    return {"name":"DeepGrocer","status":"ok"}
