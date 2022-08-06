
import aws_cdk as cdk
import aws_cdk.aws_s3 as s3
import aws_cdk.aws_iam as iam
from aws_cdk import CfnOutput, aws_lambda as lambda_, aws_lambda_event_sources as lambdaEventSource
import aws_cdk.aws_dynamodb as dynamodb


class CdkApp1Stack(cdk.Stack):

    def __init__(self, scope: cdk.App,construct_id: str, **kwargs) ->None:
        super().__init__(scope,construct_id,**kwargs)
        
        '''
        creat s3 bucket for storing images
        '''

        bucket = s3.Bucket(self, "MyBucket2232",
            removal_policy=cdk.RemovalPolicy.DESTROY,
            auto_delete_objects=True)
        CfnOutput(self, "Bucket",value= bucket.bucket_name)

        '''
        creat and attach lambda role
        '''

        lambda_role = iam.Role(self, "cdk-lambdarole",
            assumed_by= iam.ServicePrincipal("lambda.amazonaws.com"))
        lambda_role.add_to_policy(
            iam.PolicyStatement(
                effect = iam.Effect.ALLOW,
                actions=[ 
                    "rekognition:*",
                    "logs:CreateLogGroup",
                    "logs:CreateLogStream",
                    "logs:PutLogEvents",],
                resources=["*"])
        )

        '''
        creat dynamodb table for image labels
        '''

        table = dynamodb.Table(self, "cdk-db-label",
                partition_key=dynamodb.Attribute(name = "image", type=dynamodb.AttributeType.STRING),
                removal_policy= cdk.RemovalPolicy.DESTROY
                )
        CfnOutput(self, "dbTable",value= table.table_name)



        '''
        creat lambda function to trigger upon object put on s3
        '''


        lambdaf = lambda_.Function(self, "cdk-function",
                code= lambda_.Code.from_asset("lambda"),
                runtime = lambda_.Runtime.PYTHON_3_8,
                handler = "index.handler",
                role = lambda_role,
                environment= {
                    "TABLE" : table.table_name,
                    "BUCKET" : bucket.bucket_name,
                },
        )
        lambdaf.add_event_source(lambdaEventSource.S3EventSource(bucket,
                events = [s3.EventType.OBJECT_CREATED]
                ))
        
        bucket.grant_read_write(lambdaf)
        table.grant_full_access(lambdaf)





