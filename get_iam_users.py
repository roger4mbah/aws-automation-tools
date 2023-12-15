

import boto3

# Create IAM client
iam = boto3.client('iam')

# Get information about IAM users
response = iam.list_users()

# Iterate over the list of users
for user in response['Users']:
    # Get the user name
    user_name = user['UserName']
    print(user_name)
    # Get the user's last console login
    # print(iam.get_login_profile(UserName=user_name)['LoginProfile']['UserName'])
    # last_login = iam.get_login_profile(UserName=user_name)['LoginProfile']['LastLoginDate']
    # # Print the user name and last console login
    # print(f'User: {user_name}, Last Console Login: {last_login}')