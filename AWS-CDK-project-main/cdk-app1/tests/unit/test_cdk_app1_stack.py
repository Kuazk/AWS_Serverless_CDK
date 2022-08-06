import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_app1.cdk_app1_stack import CdkApp1Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_app1/cdk_app1_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkApp1Stack(app, "cdk-app1")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
