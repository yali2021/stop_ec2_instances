import boto3


def lambda_handler(event, context):
    ec2_client = boto3.client('ec2')
    # Get list of regions
    regions = [region['RegionName']
               for region in ec2_client.describe_regions()['Regions']]

    print("Regions:", regions)

    # Iterate over each region
    for region in regions:

        ec2 = boto3.resource('ec2', region_name=region)
        print("Region: ", region)

        # Get running instances only
        instances = ec2.instances.filter(
            Filters=[
                {
                    'Name': 'instance-state-name',
                    'Values': [
                        'running'
                    ]
                }
            ]
        )

        # Stop the instances
        for instance in instances:
            instance.stop()
            print('Stopped instance: ', instance.id)


