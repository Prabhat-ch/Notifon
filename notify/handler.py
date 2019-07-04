import os


def post_to_slack(event, context):

    webhook_url = os.environ['SLACK_WEBHOOK_URL']
    print(webhook_url)
    print(event)

    return
