import json
import urllib3

http = urllib3.PoolManager()

url = "https://www.uuidgenerator.net/api/version4"

def lambda_handler(event, context):
    response = http.request('GET',
                        url,
                        retries = False)
    
    
    if response.status == 200:
        return {
            'statusCode': 200,
            'body': response.data
        }
    else:
        return {
            'statusCode': response.status
        }
