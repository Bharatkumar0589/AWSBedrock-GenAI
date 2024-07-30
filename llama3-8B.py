import boto3
import json

prompt_data = """
You are impersonating as a Philosophist and write a prose on Artficial Intelligence
"""

bedrock = boto3.client(service_name='bedrock-runtime')

payload = {
    "prompt":prompt_data,
    "max_gen_len":512,
    "temperature":0.5,
    "top_p":0.9
}

body = json.dumps(payload)
model_id = "meta.llama3-8b-instruct-v1:0"
response = bedrock.invoke_model(
    modelId=model_id,
    contentType="application/json",
    accept="application/json",
    body=body
)

response_body = json.loads(response.get("body").read())
response_text = response_body['generation']
print(response_text)