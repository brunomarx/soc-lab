# Runbook: suspected access key compromise

1. Identify the key and principal from the GuardDuty finding.
2. Deactivate the key (do not delete yet).
3. Pull 7 days of CloudTrail for the key with `scripts/export_findings.py`.
4. Look for: ListBuckets, ListSecrets, GetParametersByPath, CreateUser,
   CreateServiceSpecificCredential.
5. Rotate everything the principal could reach.
6. Write up in the incident tracker.
