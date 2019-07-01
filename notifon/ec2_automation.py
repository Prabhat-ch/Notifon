# coding: utf-8
import boto3
session = boto3.Session(profile_name='pythonAutomation')
ec2 = session.resource('ec2')
key_name = 'python_automation_key'
key_path = key_name + '.pem'
key = ec2.create_key_pair(KeyName=key_name)
key.key_material
with open(key_path, 'w') as key_file:
    key_file.write(key.key_material)
import os, stat
os.chmod(key_path, stat.S_IRUSR | stat.S_IWUSR)
ec2 = session.resource('ec2')
key_name = 'python_automation_key'
key_path = key_name + '.pem'
key = ec2.create_key_pair(KeyName=key_name)
key.key_material
with open(key_path, 'w') as key_file:
    key_file.write(key.key_material)
import os, stat
os.chmod(key_path, stat.S_IRUSR | stat.S_IWUSR)
img = ec2.Image('ami-0b898040803850657')
img.name
ami_name = 'amzn2-ami-hvm-2.0.20190618-x86_64-gp2'
filters = [{'Name': 'name', 'Values': [ami_name]}]
img = list(ec2.images.fileter(Owners=['amazon'], Filters=filters)[0]
)
img = list(ec2.images.filter(Owners=['amazon'], Filters=filters)[0])
img = list(ec2.images.filter(Owners=['amazon'], Filters=filters))[0]
img.id
instances = ec2.create_instances(ImageId=img.id, KeyName=key_name, MinCount=1, MaxCount=1, InstanceType='t2.micro')
inst = instances[0]
inst.wait_until_running()
inst.reload()
inst.dns_name
inst.public_dns_name
inst.security_group
inst.security_groups
inst.describe_security_groups
response = ec2.describe_security_groups(group_id=isnt.security_groups[0].id)
sg = ec2.SecurityGroup(inst.security_groups[0].id)
sg = ec2.SecurityGroup(inst.security_groups[0].[GroupId])
sg = ec2.SecurityGroup(inst.security_groups[0][GroupId])
sg = ec2.SecurityGroup(inst.security_groups[0]['GroupId'])
sg.authorize_security_group_ingress(
IpProtocol='ssh',
FromPort=22,
ToPort=22,
CidrIp='103.214.79.122/32')
sg.authorize_ingress(
IpProtocol='ssh',
FromPort=22,
ToPort=22,
CidrIp='103.214.79.122/32')
sg.authorize_ingress(
IpProtocol='tcp',
FromPort=22,
ToPort=22,
CidrIp='103.214.79.122/32')
sg.authorize_ingress(
IpProtocol='http',
FromPort=80,
ToPort=80,
CidrIp='0.0.0.0/0')
sg.authorize_ingress(
IpProtocol='TCP',
FromPort=80,
ToPort=80,
CidrIp='0.0.0.0/0')
inst.public_dns
get_ipython().run_line_magic('history', '')
