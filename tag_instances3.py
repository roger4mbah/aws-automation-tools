import os
import boto3

def read_instance_ids_from_file(file_path):
    with open(file_path, 'r') as file:
        instance_ids = [line.strip() for line in file if line.strip()]
    return instance_ids

def read_tags_from_file(file_path):
    with open(file_path, 'r') as file:
        tags = [line.strip().split(':') for line in file if line.strip()]
    return [{'Key': key, 'Value': value} for key, value in tags]

def get_instance_tags(ec2_client, instance_id):
    response = ec2_client.describe_instances(InstanceIds=[instance_id])
    reservations = response['Reservations']
    
    if reservations:
        instance = reservations[0]['Instances'][0]
        return instance.get('Tags', [])
    else:
        return []

def update_instance_tags(ec2_client, instance_id, tags_to_add):
    ec2_client.create_tags(Resources=[instance_id], Tags=tags_to_add)

def modify_instance_tags(ec2_client, instance_id, existing_tags, new_tags):
    tags_to_modify = []

    for new_tag in new_tags:
        tag_present = any(tag['Key'] == new_tag['Key'] for tag in existing_tags)

        if not tag_present or (tag_present and existing_tags[tag_present]['Value'] != new_tag['Value']):
            tags_to_modify.append(new_tag)

    if tags_to_modify:
        ec2_client.create_tags(Resources=[instance_id], Tags=tags_to_modify)

def main():
    file_path = 'host_ids'  # Specify the file name
    tags_file_path = 'tags_to_add'  # Specify the tags file name
    ec2_client = boto3.client('ec2', region_name='us-east-1')  # Replace with your AWS region

    with open(file_path, 'r') as file:
        instance_ids = read_instance_ids_from_file(file_path)

    tags_to_add = read_tags_from_file(tags_file_path)

    for instance_id in instance_ids:
        existing_tags = get_instance_tags(ec2_client, instance_id)

        if not existing_tags: 
            update_instance_tags(ec2_client, instance_id, tags_to_add)
        else:
            modify_instance_tags(ec2_client, instance_id, existing_tags, tags_to_add)

if __name__ == "__main__":
    main()
