# AWS-CDK-project

This project uses the AWS Cloud Development Kit (CDK) to create a serverless architecture for image recognition. It consists of an S3 bucket for storing images, an AWS Lambda function for processing image uploads, and a DynamoDB table for storing image labels. The Lambda function uses Amazon Rekognition to detect labels in the uploaded images.

# Prerequisites

To deploy this project, you'll need:

AWS CLI installed and configured with your AWS credentials
Python 3.6 or later
AWS CDK installed

# Deployment Steps

Clone this repository to your local machine.

Located the project file at the directory:
```cd cdk-app1```

Install the necessary dependencies for the CDK project:
```npm install```

Install the necessary Python dependencies:
```$ pip install -r requirements.txt```

Deploy the CDK stack to your AWS account:

```$ cdk deploy```

After the deployment is completed, you'll see the created resources' outputs, such as the S3 bucket name and the DynamoDB table name.

# Usage
Upload an image to the S3 bucket. The Lambda function will be triggered automatically, and it will use Amazon Rekognition to detect labels in the image. The detected labels will be stored in the DynamoDB table.

# Cleaning Up
To delete the created resources, run:

```cdk destory ```
