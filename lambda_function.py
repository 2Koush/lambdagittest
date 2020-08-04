import json

def lambda_handler(event, context):
    print("Hello 4")

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
