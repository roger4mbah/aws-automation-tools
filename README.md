# EC2 Tags Management Script

This Python script is designed to manage tags for Amazon EC2 instances. It reads a list of EC2 instance IDs from a file (`host_ids`) and a list of tags from another file (`tags_to_add`). The script checks if the instances have existing tags and either updates or adds new tags accordingly.

## Requirements

Before using this script, ensure that you have the following requirements installed:

1. **Python:** The script is written in Python. You can download and install Python from the [official Python website](https://www.python.org/downloads/).

2. **Boto3:** Boto3 is the Amazon Web Services (AWS) SDK for Python. Install it using the following command:

    ```bash
    pip install boto3
    ```

3. **AWS CLI:** The AWS Command Line Interface (CLI) is necessary for configuring your AWS credentials. Follow the instructions in the [AWS CLI User Guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html) to install and configure the AWS CLI.

## Configuration

1. **AWS Credentials:**
   
   Make sure that your AWS credentials are configured on the machine where you run the script. You can configure credentials using the `aws configure` command. Ensure that the credentials have the necessary permissions to describe EC2 instances and create/update tags.

   ```bash
   aws configure
   ```
  ## Input Files:
  **host_ids:** This file should contain a list of EC2 instance IDs, with each ID on a separate line.<br>
  **tags_to_add:** This file should contain a list of tags to add or modify in the format key:value, with each tag on a separate line.
## How to Use
1. Clone the repository to your local machine:
```
git clone https://github.com/yourusername/ec2-tags-management.git
```
2. Navigate to the script directory:
```
cd ec2-tags-management
```
3. Edit the host_ids and tags_to_add files with your specific instance IDs and tags.<br>

4. Run the Script:
   ```
   python ec2_tags_management.py
   ```
The script will read the instance IDs and tags from the specified files, interact with AWS to manage the EC2 instance tags, and provide feedback on the process.

***Note:*** Ensure that you have the necessary permissions to describe EC2 instances and create/update tags in the AWS account.<br>

Feel free to customize the script and files according to your specific requirements. If you encounter any issues, refer to the script comments or consult the AWS Boto3 Documentation for additional guidance.
   
