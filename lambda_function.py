import json

def lambda_handler(event, context):
    print("Hello 2")

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
