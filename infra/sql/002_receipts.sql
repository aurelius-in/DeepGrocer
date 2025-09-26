CREATE TABLE IF NOT EXISTS receipts (
  id BIGSERIAL PRIMARY KEY,
  ts TIMESTAMP DEFAULT now(),
  agent TEXT NOT NULL,
  action TEXT NOT NULL,
  inputs_hash TEXT NOT NULL,
  policy_version TEXT NOT NULL,
  risk_tier TEXT NOT NULL,
  sim_summary JSONB,
  outcome JSONB,
  rollback JSONB,
  signature TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_receipts_agent_ts ON receipts(agent, ts DESC);
CREATE TABLE IF NOT EXISTS receipts (
  id BIGSERIAL PRIMARY KEY,
  ts TIMESTAMP DEFAULT now(),
  agent TEXT NOT NULL,
  action TEXT NOT NULL,
  inputs_hash TEXT NOT NULL,
  policy_version TEXT NOT NULL,
  risk_tier TEXT NOT NULL,
  sim_summary JSONB,
  outcome JSONB,
  rollback JSONB,
  signature TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_receipts_agent_ts ON receipts(agent, ts DESC);
