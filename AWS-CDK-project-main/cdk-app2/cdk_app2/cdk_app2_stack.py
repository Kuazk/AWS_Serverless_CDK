from aws_cdk import (

    Stack,
    aws_ec2 as ec2,
)
from constructs import Construct

class CdkApp2Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        '''
        Create VPC with 4 Subnet

        subnet 1 && 2: public subnet with loadbalancer node

        subnet 3 && 4: private subnet with wordpress site
        
        '''
        vpc = ec2.Vpc(self, "wordPressVPC",
                cidr = "10.3.0.0/16",

                max_azs = 2,

                subnet_configuration=[ ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PUBLIC,
                    name = "LoadBalancer",
                    cidr_mask=24
                ), ec2.SubnetConfiguration(

                    subnet_type= ec2.SubnetType.PRIVATE_WITH_NAT,
                    name = 'WordPressSite',
                    cidr_mask = 24

                )
                ]
                )

        
        '''
        
        create Security Groups
        
        '''
        loadbalancerSG = ec2.SecurityGroup(self, 'loadbaSG',
                vpc = vpc,
                allow_all_outbound= True)
        
        loadbalancerSG.add_ingress_rule(
            peer = ec2.Peer.any_ipv4(),
            connection= ec2.Port.all_traffic(),
            description= 'allow HTTP traffic'
        )

        wordPressSG = ec2.SecurityGroup(self, 'wrodPressSG',
                vpc = vpc,
                allow_all_outbound= True)
        
        wordPressSG.add_ingress_rule(
            peer= ec2.Peer.security_group_id(loadbalancerSG.security_group_id),
            connection = ec2.Port.tcp(80)
        )


        
        


        
