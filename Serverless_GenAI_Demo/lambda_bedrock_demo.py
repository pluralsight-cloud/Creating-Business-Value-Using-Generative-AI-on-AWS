import json
import boto3

boto3_invoke_bedrock = boto3.client('bedrock-runtime')

def lambda_handler(event, context):
    # TODO implement
    prompt_data="Write a tweet on SageMaker in the style of fayecloudguru"

    #Formatting the prompt before it is passed to the model
    body = json.dumps({"prompt": "Human:"+prompt_data+"\nAssistant:", "max_tokens_to_sample":300})
    
    #Define the model info
    modelId='anthropic.claude-v2'
    accept = 'application/json'
    contentType = 'application/json'
    
    #Use boto3 to invoke the model with the prompt and print the response
    response = boto3_invoke_bedrock.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)
    response_body = json.loads(response.get('body').read())
    print(response_body)

    
    
    return {
        'statusCode': 200,
    }
