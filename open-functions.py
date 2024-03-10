from fastapi import FastAPI, HTTPException, Request
from dotenv import load_dotenv
from datetime import datetime
import requests
import json
import re
import os
import logging
from pydantic import BaseModel

load_dotenv()
# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

app = FastAPI(
    title="Open Functions",
    description="Use open LLMs like Llama and Mistral and extend them with function calling capabilities.",
    version="1.0.0"
)

# Request and Response models
class FunctionCallRequest(BaseModel):
    text: str

class FunctionCallResponse(BaseModel):
    type: str = None
    name: str = None
    parameters: dict = None
    status: str = None
    timestamp: str

# Define your LLM API endpoint and auth details
LLM_ENDPOINT = os.environ.get("LLM_ENDPOINT", "https://api.localmind.ai/v1/chat/completions")
LLM_API_KEY = os.environ.get("LLM_API_KEY", "add-your-key-here")

# Define your Multimodal LLM endpoint and auth details
MULTIMODAL_ENDPOINT = os.environ.get("MULTIMODAL_ENDPOINT", "https://mllm-api.localmind.ai/v1/chat/completions")
MULTIMODAL_API_KEY = os.environ.get("MULTIMODAL_API_KEY", "add-your-key-here")

# Call the LLM model
def call_llm_api(user_input):
    logging.debug("Calling LLM API")
    # Read system prompt content from a file
    with open("SYSTEM_PROMPT", "r") as file:
        system_prompt = file.read().strip()
        logging.debug(f"System prompt read from file: {system_prompt}")

    payload = {
        "model": "localmind-pro",
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
        logging.debug(f"LLM API response: {response.json()}")
        return response.json()
    except requests.RequestException as e:
        logging.error(f"Request to LLM failed: {e}")
        return None

# Function to find and validate JSON in markdown code block
def extract_and_validate_json(text):
    logging.debug("Extracting and validating JSON from text")
    # Regex to find markdown code blocks
    matches = re.findall(r"```json(.*?)```", text, re.DOTALL)
    for match in matches:
        try:
            # Attempt to parse the code block as JSON
            parsed_json = json.loads(match)
            logging.debug(f"Valid JSON found: {parsed_json}")
            return True, parsed_json
        except json.JSONDecodeError:
            logging.warning("Invalid JSON encountered")
            continue
    return False, None

@app.post('/function_call', summary="Call LLM Function", response_model=FunctionCallResponse)
async def function_call(request: Request):
    """
    Calls the LLM API with the user input and returns the response.

    - **text**: User input text to process
    """
    request_data = await request.json()
    user_input = request_data.get('text')
    logging.info(f"Received user input: {user_input}")

    if not user_input:
        logging.error("No text provided in request")
        raise HTTPException(status_code=400, detail="No text provided")

    # Call the LLM API
    llm_response = call_llm_api(user_input)

    if llm_response is None:
        logging.error("LLM response is None")
        raise HTTPException(status_code=500, detail="LLM service unavailable")

    # Attempt to extract the message from the LLM response
    try:
        llm_message = llm_response['choices'][0]['message']['content']
        logging.info(f"LLM message extracted: {llm_message}")
    except (KeyError, IndexError, TypeError) as e:
        logging.error(f"Invalid response structure from LLM: {e}")
        raise HTTPException(status_code=500, detail="Invalid response structure from LLM")

    # Check if the LLM message contains valid JSON in a markdown code block
    json_found, json_data = extract_and_validate_json(llm_message)

    # Update to include JSON data keys as root keys and add timestamp
    response_data = json_data if json_data else {}
    response_data['timestamp'] = datetime.now().isoformat()  # Add timestamp to response

    logging.debug(f"Function call response data: {response_data}")
    return response_data
