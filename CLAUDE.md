<!-- support-first-development -->
# Support-First Development (Post-Launch Support System)

**Principle:** The AI that builds a feature is also its first support engineer. A missing support system kills more launched products than bad code. Support artifacts are minimum production deliverables — never afterthoughts.

## Rule 1 — Support playbook ships with the feature (same sprint, same conversation)

Whenever building or significantly changing a user-facing feature, create or update a support playbook alongside it in `docs/support/<feature>.md`. Do this in the SAME session as the implementation, not after launch. Each playbook documents:

- **Failure modes** users will actually hit (e.g. login: password-reset failures, expired tokens, locked accounts; payments: failed charges, missed webhooks, subscription issues)
- **Symptoms** — what the user sees, what appears in logs
- **Diagnosis steps** — how to confirm which failure mode it is
- **Documented fix** — exact resolution steps (commands, queries, admin actions)
- **Escalation criteria** — when this is NOT a known issue

If the AI builds the feature, the AI documents how to support that feature. If `docs/support/` doesn't exist yet, create it.

## Rule 2 — Connect the system to production signals

Every feature ships with the observability needed for real-time support: structured error logging, webhook failure handling, and alerting hooks. A support system that learns about problems "tomorrow" is not a support system. When debugging a production issue: first check the relevant playbook — resolve per playbook if documented, and UPDATE the playbook with the new case if not. The playbook must grow with every incident; the system gets smarter every week.

## Rule 3 — Three support tiers, defined before the first customer signs up

- **Tier 1 — Automated resolution:** Known issue + documented fix → automate it (self-service flows, auto-remediation, clear error messages with recovery paths). Target: 60–70% of support volume never reaches a human.
- **Tier 2 — Assisted triage:** Unknown issue → package the full context (logs, affected user, reproduction, impact) and escalate WITH a recommendation. The human decides, the fix gets executed, the playbook grows.
- **Tier 3 — Incident response:** Multiple users affected, or security/data integrity involved → trigger the incident playbook: who gets notified, what gets locked down, how customers are communicated with. This playbook must exist BEFORE launch — if this repo has none, flag it as a launch blocker.

## Definition of Done (launch-ready)

A feature is not production-ready until: (1) its support playbook exists, (2) its failure modes emit observable signals, and (3) it is mapped to a support tier. Treat these as part of the deliverable, equal in rank to passing tests.
<!-- /support-first-development -->
