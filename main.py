import boto3, os
import json, sys # Only used for manual execution via cli not AWS Lambda
from botocore.config import Config

def lambda_handler(context,event):
    # Increase max_attempts due to limit threshold being tripped
    config = Config(
        retries = dict(
            max_attempts = 10   # docs say default is 5
        )
    )
    snapshotId = context['SnapshotId']
    ec2 = boto3.client('ec2', region_name=os.environ['AWS_REGION'])

    for snapId in snapshotId:
        try:
            ec2.delete_snapshot(SnapshotId=snapId)
        except Exception as e:
            print(e)
        else:
            print("Removed old snapshots based on expired Retention tag")

if __name__ == '__main__':
    context = json.load( sys.stdin )
    event = ""
    lambda_handler(context,event)
