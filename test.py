import json

def lambda_handler(event, context):
    print("Hello 1")

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
