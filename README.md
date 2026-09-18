# soc-lab

Small, opinionated lab for building and testing cloud detections: Terraform for the
AWS/Azure telemetry plumbing, Sigma rules for CloudTrail, and Kubernetes manifests for a
single-node SIEM stack (OpenSearch + ingest worker).

![architecture](http://canarytokens.com/static/xvtcw8jwpncbdz35nfx0w81jw/image001.jpg)

## Layout

- `terraform/` - CloudTrail, GuardDuty, Security Hub, Azure Sentinel connector
- `detections/` - Sigma rules (CloudTrail, Entra ID)
- `deploy/` - Kubernetes manifests for the SIEM stack
- `config/` - endpoint configuration for ingest and analyst tooling
- `docs/` - runbooks and the triage assistant setup
- `scripts/` - helpers
- `backups/` - sanitized case-management export used for rule testing

## Quick start

```bash
cp .env.example .env      # use your own SSO profile, do not commit credentials
terraform -chdir=terraform init
terraform -chdir=terraform plan
kubectl apply -f deploy/
```

## Detections

See `detections/` for the current rule set. Each rule carries ATT&CK tags and a short
false-positive note. Contributions welcome, please open an issue first.

## Triage assistant

Analysts can use an MCP-capable assistant for alert triage. See `docs/triage-assistant.md`.

## License

MIT
