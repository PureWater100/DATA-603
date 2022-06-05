### Goal:
### Upload data to Amazon S3 Object Storage, and access directly from your DataBricks environment.
### Purpose:
### S3 is a type of Object Storage service provide by AWS. Object storage is a key ingredient of any cloud based modern day Big Data system. It has multiple uses:
### A storage platform for a data lake.
### Archival Store
### Disaster Recovery
### Backup
### Through this exercise, you will get experience using S3 to store data, and then leveraging it in the DataBricks platform. You can use the concept in your projects: For example, you can store your data on S3 (instead of your pc) and then connect from Databricks directly to S3. You can "pull" data into Databricks in this manner for further transformation, processing, and creation of your Big Data environments.
### Step 1 
### I will demonstrate these steps in class, and you can follow along:
### Download the AWS CLI, by following the steps here: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
### Configure the cli with this key and secret pair:
### Key: AKIASR3KTGDUA3M5J3F6
### Secret: 4bOAIZIVhxtlRNSIqKZxHRfzpQ9KexSdPmyJZiUT
### If you are asked to supply a region, enter: us-east-2
### Upload a file to AWS bucket named: data603
### Put your name in the upload path so that the data in the bucket is organized properly. e.g.  JohnsData/weather-data.csv
### List your file using the ls command to ensure your file has been uploaded.
### Step 2
### Access your data from the DataBricks Envrionment
### Open the attached file: S3-Demo.py
### Modify the code with the name of your file.
### Ensure you can access data from S3.
### Publish your notebook so the instructor can check your work.
