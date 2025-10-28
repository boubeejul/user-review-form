import json
import os
import boto3

dynamodb = boto3.resource('dynamodb')
table_name = os.environ["TABLE_NAME"]
table = dynamodb.Table('UsersReviews')

def handler(event, context):
    id = event.get("id")
    username = event.get("username")
    title = event.get("title")
    date = event.get("date")
    message = event.get("message")

    try:
        table.put_item(
            Item={
                'ID': id,
                'username': username,
                'title': title,
                'date': date,
                "message": message
            }
        )

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Avaliação salva com sucesso.'})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }
