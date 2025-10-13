import json

def lambda_handler(event, context):
    """
    A simple AWS Lambda function that returns a success message.
    """
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Success! The Lambda function executed correctly.'
        })
    }
