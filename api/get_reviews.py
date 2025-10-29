import json
import os
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table_name = os.environ["TABLE_NAME"]
table = dynamodb.Table(table_name)

def handler(event, context):
    try:
        reviews = table.query(
            KeyConditionExpression=Key('PK').eq('REVIEW')
        )

        return {
            'statusCode': 200,
            'body': json.dumps({'reviews': reviews['Items']})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }
