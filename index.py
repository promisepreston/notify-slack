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
def handler(event, context):
    url = WEBHOOK_URL
    payload = extractMessage(event["Records"][0]["Sns"]["Message"])
    msg = {
			"channel": CHANNEL,
			"username": USERNAME,
			"text": payload,
			"icon_emoji": ICON_EMOJI,
    }

    encoded_msg = json.dumps(msg).encode("utf-8")
    print(encoded_msg)
    resp = http.request("POST", url, body=encoded_msg)
    print(
			{
				"message": payload,
				"status_code": resp.status,
				"response": resp.data,
			}
    )

# Format json payload
def extractMessage(msg):
	try:
		alarmDic = json.loads(msg)
	except:
		print("Error while converting payload to json")
		return
	return "AlarmName: %s \AlarmDescription: %s" % (alarmDic["AlarmName"], alarmDic["AlarmDescription"])
