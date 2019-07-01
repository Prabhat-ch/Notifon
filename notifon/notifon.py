import boto3
session = boto3.Session(profile_name='pythonAutomation')
ec2 = session.resource('ec2')
key_name = 'python_automation_key'
key_path = key_name + '.pem'
key = ec2.create_key_pair(KeyName=key_name)
with open(key_path, 'w') as key_file:
    key_file.write(key.key_material)
import os, stat
os.chmod(key_path, stat.S_IRUSR | stat.S_IWUSR)
img = ec2.Image('ami-0b898040803850657')
img.name
ami_name = 'ami-0b898040803850657'
filters = [{'Name': 'name', 'Values': [ami_name]}]
list(ec2.images.filter(Owners=['amazon'], Filters=filters))
ami_name = 'amzn2-ami-hvm-2.0.20190618-x86_64-gp2'
list(ec2.images.filter(Owners=['amazon'], Filters=filters))
filters = [{'Name': 'name', 'Values': [ami_name]}]
list(ec2.images.filter(Owners=['amazon'], Filters=filters))
instances = ec2.create_instances(ImageId=ami_name, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key_name)
list(ec2.images.filter(Owners=['amazon'], Filters=filters))
img = list(ec2.images.filter(Owners=['amazon'], Filters=filters))[0]
img
instances = ec2.create_instances(ImageId=ami_name, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key_name)
instances = ec2.create_instances(ImageId=img, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key_name)
img.id
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key_name)
instances
inst = instances[0]
inst
inst.public_dns_name
inst.wait_until_running()
inst.reload()
inst.public_dns_name
inst.security_groups
inst.create_security_group(GroupName='ssh_in')
ec2.create_security_group(GroupName='ssh_in')
ec2.create_security_group(Description='let ssh in', GroupName='ssh_in')
response = ec2.create_security_group(Description='let ssh in', GroupName='ssh_in')
response = ec2.create_security_group(Description='let ssh in', GroupName='let_ssh_in')
response
response.type()
response.id
ec2.security_group_ingress(
GroupId=respose.id,
IpPermissions=[
{'IpProtocol': 'tcp',
'FromPort': 22,
'ToPort': 22,
'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}]
)
ec2.authorize_security_group_ingress(
GroupId=respose.id,
IpPermissions=[
{'IpProtocol': 'tcp',
'FromPort': 22,
'ToPort': 22,
'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}]
)
