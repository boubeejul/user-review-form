import json
import os
import boto3
from uuid import uuid4

dynamodb = boto3.resource('dynamodb')
table_name = os.environ["TABLE_NAME"]
table = dynamodb.Table(table_name)

def handler(event, context):
    body = json.loads(event["body"])
    print(body)
    username = body.get("username")
    title = body.get("title")
    date = body.get("date")
    message = body.get("message")


    try:
        table.put_item(
            Item={
                'PK': 'REVIEW',
                'SK': f'REVIEW_ID#{str(uuid4())}',
                'username': username,
                'title': title,
                'date': date,
                "message": message
            }
        )

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Sua avaliação foi enviada com sucesso.'}),
            "headers": {
                "Content-Type": "application/json"
            }
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }
