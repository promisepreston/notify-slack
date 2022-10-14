#!/usr/bin/python3.9
import json
import os
import urllib3

http = urllib3.PoolManager()

# Set environment variables
WEBHOOK_URL = os.environ.get("SLACK_WEBHOOK_URL")
CHANNEL = os.environ.get("SLACK_CHANNEL")
USERNAME = os.environ.get("SLACK_USERNAME")
ICON_EMOJI = os.environ.get("SLACK_ICON_EMOJI")

# Define lambda function
def lambda_handler(event, context):
    url = WEBHOOK_URL
    msg = {
        "channel": CHANNEL,
        "username": USERNAME,
        "text": event["Records"][0]["Sns"]["Message"],
        "icon_emoji": ICON_EMOJI,
    }

    encoded_msg = json.dumps(msg).encode("utf-8")
    resp = http.request("POST", url, body=encoded_msg)
    print(
        {
            "message": event["Records"][0]["Sns"]["Message"],
            "status_code": resp.status,
            "response": resp.data,
        }
    )
