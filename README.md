# aws-python-greengrass-lambda
Python codes for local lambda function running in Edge gateway

This is a sample showcase of lambda function that will be running in an edge gateway running AWS Greengrass software.
This project is meant to simulate writing a JSON payload to data-stream.

## What is AWS greengrass and why deploy Lambda function on greengrass?
AWS IoT Greengrass is software that extends cloud capabilities to local devices. This enables devices to collect and analyze data closer to the source of information, react autonomously to local events, and communicate securely with each other on local networks. Local devices can also communicate securely with AWS IoT Core and export IoT data to the AWS Cloud. With a lambda function running locally in an edge gateway, it reduces the cost of cloud services as well.


## Deploying lambda function
Upload the zip file onto AWS lambda console, ensure that the function handler adheres to the form **<file-name.handler-name>**

## create-data-stream-py
This is a python deployment package to create a data stream named **StreamFromPython** and export to AWS kinesis data stream named **PythonKinesisStream** . 
The Kinesis data stream can then be used by some other consumer like Amazon Simple Storage Service (Amazon S3), Amazon Redshift, Amazon Elasticsearch Service (Amazon ES), or Splunk.
For more details, visit [AWS Kinesis data stream documentation](https://docs.aws.amazon.com/streams/latest/dev/amazon-kinesis-consumers.html)


## write-data-stream-py
This is a python deployment package to write a sample JSON to the data stream named **StreamFromPython** every 5 seconds. A sequence number will be returned with a successful write.

## read-data-stream-py
This python deployment package will attempt to read the JSON payload from the data stream. Further manipulation of JSON payload can be done here.

## json-transformation.py
This is a sample python script that sanitise a bulky JSON payload to a light weight payload





