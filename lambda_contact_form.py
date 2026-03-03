import boto3
import json
import os

ses = boto3.client('ses', region_name='eu-north-1')

SENDER = os.environ.get('SENDER_EMAIL')

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])

        name = body.get('name')
        email = body.get('email')
        message = body.get('message')

        subject = f"New message from {name}"
        body_text = f"From: {name} <{email}>\n\n{message}"

        response = ses.send_email(
            Source=SENDER,
            Destination={'ToAddresses': [SENDER]},
            Message={
                'Subject': {'Data': subject},
                'Body': {'Text': {'Data': body_text}}
            }
        )

        return {
            'statusCode': 200,
            'body': json.dumps({'status': 'Email sent successfully'})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
