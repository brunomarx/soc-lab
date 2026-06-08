# soc-lab

Small, opinionated lab for building and testing cloud detections: Terraform for the
AWS/Azure telemetry plumbing, Sigma rules for CloudTrail, and Kubernetes manifests for a
single-node SIEM stack (OpenSearch + ingest worker).

Status: early. Expect breaking changes.

## Layout

- `terraform/` - CloudTrail, GuardDuty, log bucket
- `detections/` - Sigma rules (CloudTrail)
- `deploy/` - Kubernetes manifests for the SIEM stack
- `scripts/` - helpers
