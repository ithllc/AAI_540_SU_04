import os
import boto3
import jupyter
import nbconvert
import sagemaker

# save Amazon information
region = boto3.Session().region_name
role = sagemaker.get_execution_role()
sagemaker_session = sagemaker.Session()
s3 = boto3.client('s3', region_name=sagemaker_session.boto_region_name)

bucket_name = ''
boto3_session = boto3.Session()
get_S3_Bucket = boto3_session.resource('s3')
for bucket in get_S3_Bucket.buckets.all():
    print(f'Python Script Bucket Name: {bucket.name}')
    bucket_name = bucket.name

# List of notebooks
notebooks = ['01_Set_Up_Dependencies.ipynb', '02_Set_Up_S3.ipynb', '03_Preprocess_Data.ipynb', '04_Set_Up_Athena.ipynb', '06_Split_Data_and_Set_Up_Feature_Store.ipynb', '07_Build_Train_Deploy_Model_and_Perform_Model_Monitoring.ipynb']

# Output directory
output_dir = 's3://{}/'.format(bucket_name)


for notebook in notebooks:
    # Convert the notebook to a Python script
    os.system(f"jupyter nbconvert --to script '{notebook}' --output-dir='{output_dir}'")

    # Get the script name
    script_name = notebook.replace('.ipynb', '.py')

    # Upload the script to S3
    s3.upload_file(f"{output_dir}/{script_name}", bucket_name, script_name)
