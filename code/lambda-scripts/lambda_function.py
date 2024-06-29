import os
import subprocess
import boto3
import time

def lambda_handler(event, context):
    # Install ipython
    subprocess.call(['pip3', 'install', 'ipython'])
    
    bucket_name = ''
    boto3_session = boto3.Session()
    get_S3_Bucket = boto3_session.resource('s3')
    for bucket in get_S3_Bucket.buckets.all():
        if 'python-script' in bucket.name:
            bucket_name = bucket.name
            print(f"S3 Bucket for python script already exists: {bucket_name}")
        break

    # Set the output directory for the scripts
    output_dir = 's3://{}/'.format(bucket_name)

    # Assuming the scripts are stored in S3, download the first script
    s3 = boto3.client('s3')
    s3.download_file(bucket_name, '01_Set_Up_Dependencies.py', '/tmp/01_Set_Up_Dependencies.py')
    
    # Run the script using ipython
    subprocess.call(['ipython', '/tmp/01_Set_Up_Dependencies.py'])
    
    # List of python scripts converted from jupyter notebooks
    python_scripts = ['01_Set_Up_Dependencies.py', '02_Set_Up_S3.py', '03_Preprocess_Data.py', '04_Set_Up_Athena.py', '06_Split_Data_and_Set_Up_Feature_Store.py', '07_Build_Train_Deploy_Model_and_Perform_Model_Monitoring.py']

    # Trigger the next function (could be via SNS or direct Lambda invoke)
    # Direct Lambda invoke
    lambda_client = boto3.client('lambda')
    # Get the index of the current script in the list
    current_script_index = python_scripts.index('01_Set_Up_Dependencies.py')
    # Check if there is a next script
    if current_script_index < len(python_scripts) - 1:
        next_script_name = python_scripts[current_script_index + 1]
        lambda_client.invoke(
            FunctionName='run_next_script',
            InvocationType='Event',
            # Pass the next script name from the list
            Payload='{"script_name": "' + next_script_name + '"}'
        )

def run_next_script(event, context):
    # Install ipython
    subprocess.call(['pip', 'install', 'ipython'])
    
    bucket_name = ''
    boto3_session = boto3.Session()
    get_S3_Bucket = boto3_session.resource('s3')
    for bucket in get_S3_Bucket.buckets.all():
        bucket_name = bucket.name
        break

    # Set the output directory for the scripts
    output_dir = 's3://{}/'.format(bucket_name)

    s3 = boto3.client('s3')

    # Extract script name from the event
    script_name = event.get('script_name')
    # Logic to select the next script based on script_name and execute it
    if script_name == '02_Set_Up_S3.py':
        # Execute the code for script 02_Set_Up_S3.py

        # Assuming the scripts are stored in S3, download the first script
        s3.download_file(output_dir, '02_Set_Up_S3.py', '/tmp/02_Set_Up_S3.py')

        # Run the script using ipython
        subprocess.call(['ipython', '/tmp/02_Set_Up_S3.py'])
    elif script_name == '03_Preprocess_Data.py':
        # Execute the code for script 03_Preprocess_Data.py

        # Assuming the scripts are stored in S3, download the first script
        s3.download_file(output_dir, '03_Preprocess_Data.py', '/tmp/03_Preprocess_Data.py')

        # Run the script using ipython
        subprocess.call(['ipython', '/tmp/03_Preprocess_Data.py'])
    elif script_name == '04_Set_Up_Athena.py':
        # Execute the code for script 04_Set_Up_Athena.py

        # Assuming the scripts are stored in S3, download the first script
        s3.download_file(output_dir, '04_Set_Up_Athena.py', '/tmp/04_Set_Up_Athena.py')

        # Run the script using ipython
        subprocess.call(['ipython', '/tmp/04_Set_Up_Athena.py'])
    elif script_name == '06_Split_Data_and_Set_Up_Feature_Store.py':
        # Execute the code for script 06_Split_Data_and_Set_Up_Feature_Store.py

        # Assuming the scripts are stored in S3, download the first script
        s3.download_file(output_dir, '06_Split_Data_and_Set_Up_Feature_Store.py', '/tmp/06_Split_Data_and_Set_Up_Feature_Store.py')

        # Run the script using ipython
        subprocess.call(['ipython', '/tmp/06_Split_Data_and_Set_Up_Feature_Store.py'])
    elif script_name == '07_Build_Train_Deploy_Model_and_Perform_Model_Monitoring.py':
        # Execute the code for script 07_Build_Train_Deploy_Model_and_Perform_Model_Monitoring.py

        # Assuming the scripts are stored in S3, download the first script
        s3.download_file(output_dir, '07_Build_Train_Deploy_Model_and_Perform_Model_Monitoring.py', '/tmp/07_Build_Train_Deploy_Model_and_Perform_Model_Monitoring.py')

        # Run the script using ipython
        subprocess.call(['ipython', '/tmp/07_Build_Train_Deploy_Model_and_Perform_Model_Monitoring.py'])