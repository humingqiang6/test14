def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': 'Hello from Lambda! Request ID: ' + context.aws_request_id
    }