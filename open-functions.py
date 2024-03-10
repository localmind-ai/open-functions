from fastapi import FastAPI, HTTPException, Request
from datetime import datetime
import requests
import json
import re
import os

app = FastAPI()

# Define your LLM API endpoint and auth details
LLM_ENDPOINT = os.environ.get("LLM_ENDPOINT", "https://api.localmind.ai/v1/chat/completions")  # Fallback to Localmind AI endpoint if not set
LLM_API_KEY = os.environ.get("LLM_API_KEY", "add-your-key-here")

# Define your Multimodal LLM endpoint and auth details
MULTIMODAL_ENDPOINT = os.environ.get("MULTIMODAL_ENDPOINT", "https://mllm-api.localmind.ai/v1/chat/completions") 
MULTIMODAL_API_KEY = os.environ.get("MULTIMODAL_API_KEY", "add-your-key-here")

# Call the LLM model
def call_llm_api(user_input):
    # Read system prompt content from a file
    with open("SYSTEM_PROMPT", "r") as file:
        system_prompt = file.read().strip()

    payload = {
        "model": "localmind-pro",  # Replace with actual model version if needed
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {LLM_API_KEY}"
    }
    try:
        response = requests.post(LLM_ENDPOINT, json=payload, headers=headers)
        return response.json()
    except requests.RequestException as e:
        print(f"Request to LLM failed: {e}")
        return None
        
# Function to find and validate JSON in markdown code block
def extract_and_validate_json(text):
    # Regex to find markdown code blocks
    matches = re.findall(r"```(.*?)```", text, re.DOTALL)
    for match in matches:
        try:
            # Attempt to parse the code block as JSON
            parsed_json = json.loads(match)
            return True, parsed_json  # Return True and the parsed JSON, if successful
        except json.JSONDecodeError:
            continue  # If it's not valid JSON, continue to check other matches
    return False, None  # Return False if no valid JSON code block was found

@app.post('/function_call')
async def function_call(request: Request):
    request_data = await request.json()
    user_input = request_data.get('text')

    if not user_input:
        raise HTTPException(status_code=400, detail="No text provided")

    # Call the LLM API
    llm_response = call_llm_api(user_input)

    # Attempt to extract the message from the LLM response
    try:
        llm_message = llm_response['choices'][0]['message']['content']
    except (KeyError, IndexError, TypeError):
        raise HTTPException(status_code=500, detail="Invalid response structure from LLM")

    # Check if the LLM message contains a valid JSON in a markdown code block
    json_found, json_data = extract_and_validate_json(llm_message)

    response_data = {
        "response": llm_message,
        "valid_json_found": json_found,
        "json_data": json_data,
        "timestamp": datetime.now().isoformat()  # Add the current timestamp
    }

    return response_data
