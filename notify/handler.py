import os
import requests

def post_to_slack(event, context):

    webhook_url = os.environ['SLACK_WEBHOOK_URL']

    slack_message = "{detail[Description]} - at time: {time}".format(**event)
    data = {"text": slack_message}
    requests.post(webhook_url, json=data)
    print(webhook_url)
    print(event)

    return
