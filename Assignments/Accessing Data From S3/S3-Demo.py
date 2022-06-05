# Databricks notebook source
# Introduction to S3: https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html
# Organizations store data in "buckets"
# Our bucket name is data603
aws_bucket_name = "data603"

# our key and secret to be used for this class only.
access_key =  "AKIASR3KTGDUA3M5J3F6"
secret_key =  "will be given in hw announcement"
aws_region = "us-east-2"

# we will mount the s3 bucket to this location within our databricks environment.
mount_name = "s3mount"

# lets "mount" the bucket
dbutils.fs.mount("s3a://%s:%s@%s" % (access_key, secret_key, aws_bucket_name), "/mnt/%s" % mount_name)
display(dbutils.fs.ls("/mnt/%s" % mount_name))


# COMMAND ----------

# Let's list the files in the test folder of the bucket.
display(dbutils.fs.ls("/mnt/%s/test/" % mount_name))

# COMMAND ----------

# Let's read a file directly from S3!

df = spark.read.text("/mnt/%s/test/mnm_dataset.csv" % mount_name)
df.show()
