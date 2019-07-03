# coding: utf-8
import boto3
session = boto3.Session(profile_name='pythonAutomation')
as_client = session.client('autoscalling')
as_client = session.client('autoscaling')
as_client.describe_auto_scalling_groups()
as_client.describe_auto_scaling_groups()
as_client.describe_policy()
as_client.describe_policies()
as_client.execute_policy(AutoScalingGroupName='TestAG', PolicyName='Increase Group Size')
