# DeepGrocer

**In a nutshell:** DeepGrocer is an agentic retail ops platform that senses store signals, forecasts demand, automates replenishment, optimizes planograms/labor/pricing, orchestrates pick-pack/substitutions/last-mile/checkout, manages recalls/shrink/energy, and writes signed, policy-backed receipts.

---

## What it is

DeepGrocer is a **control plane** for grocery operations. It connects cameras, POS, scales, IoT, e-com, and supply feeds; runs **agents** that decide and act in real time; and logs every change with **policy-as-code** receipts so autonomy can safely ramp over time.

---

## The 4 main use cases

| Use case                                     | What it does                                                                                                           | Outcomes (typical)                                                                   |
| -------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| **1) Store Floor Efficiency**                | Detects OOS and facing gaps, assigns optimized restock tasks, forecasts queues and opens lanes, coaches self-checkout. | +1–2.5 pts on-shelf availability; −20–40% front-end wait; +8–12% labor productivity. |
| **2) Fresh & Supply Optimization**           | Sub-day demand sensing, MPC replenishment, dynamic markdowns, cold-chain guard, donation routing.                      | −15–30% perishables shrink; higher fill rates; faster time-to-shelf.                 |
| **3) E-com Pick, Substitution & Last-mile**  | Batches pick paths, selects high-acceptance subs, routes deliveries across gig/BOPIS/white-glove.                      | −15–25% refunds; +10–20% UPH; −8–12% delivery cost/order.                            |
| **4) Governance, Safety & Profit Integrity** | Price/promo guardrails, recall trace, vendor scorecards, energy optimization, signed audit receipts.                   | Fewer compliance incidents; faster recall containment; −6–10% energy spend.          |

> Numbers are sanity-check ranges seen in mature autonomy programs; validate with your pilots.

---

## Most likely user stories (4 personas)

1. **Store Manager:**
   *As a store manager, I want real-time tasks for stocking, markdowns, and queues so the team focuses on the next most valuable action, and I can prove every change with receipts.*

2. **Supply/Category Planner:**
   *As a planner, I want sub-day forecasts and MPC orders that respect DC capacity and truck windows so I raise in-stock without blowing working capital.*

3. **E-com Ops Lead:**
   *As an e-com lead, I want optimal pick waves, high-acceptance substitutions, and SLA-aware delivery routing so I hit on-time targets at the lowest cost.*

4. **CFO/Compliance (or VP Ops):**
   *As finance/compliance, I want every price, promo, markdown, chargeback, and refund to produce a signed, policy-backed receipt so we can scale autonomy with trust and pass audits quickly.*

---

## System flow (end-to-end)

```mermaid
flowchart LR
  subgraph Signals
    POS[POS & Payments]
    Cams[Cameras & Shelf Sensors]
    IoT[Scales & IoT (temp, energy)]
    Ecom[E-com Orders & Sessions]
    Supply[ASNs, DC, Transport]
  end

  subgraph ControlPlane[DeepGrocer Control Plane]
    Policy[Policy-as-Code & Risk Tiers]
    FS[Feature/Memory Store]
    Orchestrator[Agent Orchestrator]
    Receipts[Signed Audit Receipts]
  end

  subgraph Agents
    ShelfVision[ShelfVision]
    TaskRouter[Task Router]
    QueueFlow[QueueFlow]
    Replen[MPC Replenisher]
    PricePulse[Price & Markdown]
    PickPack[Pick-Pack Coach]
    SubGen[Substitution Genius]
    Router[Last-Mile Router]
    ColdGuard[Cold-Chain Guard]
    Recall[Recall & Trace]
    Energy[Energy Optimizer]
    Vendor[Vendor Scorecards]
  end

  subgraph Actuators[Actuation Targets]
    Handhelds[Handheld Tasks]
    Labels[ESL / Labels / POS]
    WMS[WMS / TMS]
    Comms[Staff & Customer Comms]
  end

  Signals --> ControlPlane
  ControlPlane --> Agents
  Agents --> Policy
  Policy --> Agents
  Agents --> Actuators
  Agents --> Receipts
  Receipts --> FS
  FS --> Agents
```

**How to read it:** Signals stream into the **Control Plane**. The **Orchestrator** activates agents within policy and risk limits. Agents act on store systems and people, emit **receipts**, and learn from outcomes via the memory store.

---

## Agent catalog (concise)

| Agent                         | Purpose                                                          | Primary KPIs                     |
| ----------------------------- | ---------------------------------------------------------------- | -------------------------------- |
| **ShelfVision**               | Detect OOS, phantom inventory, facing gaps from cameras/sensors. | On-shelf %, restock latency.     |
| **Task Router**               | Bundle/sequence tasks with ideal pick paths; photo proof.        | Tasks/hour, travel time.         |
| **QueueFlow**                 | Forecast front-end congestion; open lanes, steer to SCO.         | Wait time, SCO interventions.    |
| **Self-Checkout Coach**       | Auto-resolve SCO exceptions; reduce attendant calls.             | AHT, attendant touches.          |
| **Demand Sensing**            | Sub-day SKU-store forecasts from POS, weather, events.           | MAPE, OSA, waste.                |
| **MPC Replenisher**           | Model-predictive ordering respecting DC/truck/backroom.          | Fill rate, stockouts, DOH.       |
| **Planogram Enforcer**        | Compare realogram vs plan; propose feasible swaps.               | Compliance %, sales lift.        |
| **Price Pulse**               | Elasticity-aware price/markdown decisions with guardrails.       | Margin, promo ROI, sell-through. |
| **Smart Markdown**            | Time-window markdowns for perishables to sell not spoil.         | Shrink %, gross margin return.   |
| **Cold-Chain Guard**          | Monitor temp IoT; predict spoilage; auto claims.                 | Temp excursions, food safety.    |
| **Pick-Pack Coach**           | Batch waves, shortest paths, tote staging.                       | UPH, cycle time.                 |
| **Substitution Genius**       | Choose subs using taste graph & accept history.                  | Refund rate, NPS.                |
| **Last-Mile Router**          | Choose courier/gig/BOPIS; merge store + MFC.                     | On-time %, cost/order.           |
| **Recall & Trace**            | Lot traceback; isolate, notify, refund.                          | Time-to-contain, closure rate.   |
| **Shrink Sentinel**           | Detect loss patterns; soft interventions.                        | Unknown shrink, incidents.       |
| **Energy Optimizer**          | Trim HVAC/lighting peaks within comfort.                         | kWh, peak demand.                |
| **Vendor Scorecards**         | Audit on-time/fill/damage; draft chargebacks.                    | Recovery \$, OTIF %.             |
| **Member/Offer Personalizer** | Household-level offers, fuel optimization.                       | Basket size, redemption, churn.  |
| **Service Copilot**           | Resolve tickets; refunds/credits under policy.                   | AHT, CSAT, leakage.              |
| **Receipt Ledger**            | Sign every autonomous action with policy version & sim.          | Audit pass rate, autonomy tier.  |

---

## User flow by role

1. **Before store open (D-1 night / pre-open):** Demand Sensing + MPC Replenisher finalize orders and dock slots; Planogram Enforcer emits deltas; Labor plan set; labels pre-priced.
2. **Open-to-close loop:** ShelfVision + QueueFlow sense; Task Router dispatches; Smart Markdown and Price Pulse act within policy; Pick-Pack Coach and Substitution Genius handle e-com; Last-Mile Router hits SLAs; Cold-Chain Guard and Shrink Sentinel protect margins.
3. **Close:** Waste & donation routing; Realogram update; receipts consolidated; models learn and risk tiers widen where safe.

---

## Architecture (high level)

* **Ingest:** Kafka (or Pub/Sub), S3/ADLS, OpenTelemetry events.
* **Compute:** Python/Typescript agents on a graph runtime (e.g., LangGraph-style) with async workers.
* **Models:** Vision (shelf, queue), forecasting (temporal + exogenous), routing/optimization (MIP/MPC), policy RL where applicable.
* **Policy:** OPA-style policy-as-code with risk tiers; every action requires a **pre-flight sim** and writes a **receipt** (hash, actor, inputs, policy version, rollback).
* **Surfaces:** Store handheld app, Ops dashboard, Planner workspace, Receipts explorer.

---

## Getting started (dev)

```bash
# 1) clone
git clone https://github.com/<org>/deepgrocer.git
cd deepgrocer

# 2) run services (dev compose includes Kafka + Postgres + MinIO + UI)
make up

# 3) seed demo data (synthetic store day)
make seed

# 4) start agents (subset)
make agents shelfvision task-router queueflow mpc price-pulse

# 5) open UI
open http://localhost:3000
```

**Config:** see `./config/policy/` for guardrails (pricing, markdown, labor), `./config/routing/` for MIP/MPC params, and `./config/vision/` for detection thresholds.

---

## Telemetry & receipts

* Every agent action emits: `{actor, inputs_hash, policy_version, risk_tier, sim_summary, decision, actuation_target, outcome, rollback}`.
* Receipts are **append-only** (WORM) and queryable by time, store, SKU, agent, or policy version.

---

## Roadmap (cut to ship)

* [ ] Pilot bundle: ShelfVision + Task Router + Smart Markdown + QueueFlow.
* [ ] E-com bundle: Pick-Pack Coach + Substitution Genius + Last-Mile Router.
* [ ] Governance bundle: Price Pulse + Recall & Trace + Receipt Explorer.
* [ ] Planner bundle: Demand Sensing + MPC Replenisher + Planogram Enforcer.

---

## License

TBD (Apache-2.0 suggested for code, separate license for models).

---

## Credits

Designed with operators in mind. Built for measurable lifts and provable safety.
