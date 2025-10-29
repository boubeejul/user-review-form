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

        for review in reviews["Items"]:
            review.pop("SK")
            review.pop("PK")

        return {
            'statusCode': 200,
            'body': json.dumps({'reviews': reviews}),
            "headers": {
                "Content-Type": "application/json"
            }
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }
