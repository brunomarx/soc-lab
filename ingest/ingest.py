"""Pull CloudTrail objects from S3 and index them into OpenSearch."""
import gzip, json, os
import boto3
import requests

BUCKET = os.environ["LOG_BUCKET"]
OS_URL = os.environ.get("OPENSEARCH_URL", "http://localhost:9200")

s3 = boto3.client("s3")


def objects(prefix="AWSLogs/"):
    pag = s3.get_paginator("list_objects_v2")
    for page in pag.paginate(Bucket=BUCKET, Prefix=prefix):
        for o in page.get("Contents", []):
            yield o["Key"]


def records(key):
    body = s3.get_object(Bucket=BUCKET, Key=key)["Body"].read()
    for r in json.loads(gzip.decompress(body))["Records"]:
        yield r


def main():
    for key in objects():
        for r in records(key):
            requests.post(f"{OS_URL}/cloudtrail/_doc", json=r, timeout=10)


if __name__ == "__main__":
    main()
