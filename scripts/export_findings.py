#!/usr/bin/env python3
"""Export GuardDuty findings to JSON lines for rule replay."""
import json
import boto3

gd = boto3.client("guardduty")


def main():
    for det in gd.list_detectors()["DetectorIds"]:
        ids = gd.list_findings(DetectorId=det)["FindingIds"]
        if ids:
            for f in gd.get_findings(DetectorId=det, FindingIds=ids)["Findings"]:
                print(json.dumps(f, default=str))


if __name__ == "__main__":
    main()
