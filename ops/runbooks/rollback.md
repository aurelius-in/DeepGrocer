Rollback Runbook

1) Pause orchestrator: make agents
2) Revert policy bounds if needed (config/policy/*)
3) Identify impacted decisions in /api/receipts/latest and follow each rollback.hint
4) Verify state, then resume orchestrator: make agents

