from flask import Flask, request, jsonify
from datetime import datetime
import requests
import json
import re

app = Flask(__name__)

# Define your LLM API endpoint and auth details
LLM_BASE_URL = "https://example-api.localmind.ai/v1/chat/completions"  # Update this with the actual API endpoint of your LLM. It should be OpenAI-compatible with the /chat/completions or /v1/chat/completions endpoint.
LLM_API_KEY = "your_llm_api_key_here"  # Replace with your actual API key.

# Define your Multimodal LLM endpoint and auth details
MLLM_BASE_URL = "add your multimodal LLM endpoint URL here"
MLLM_API_KEY = "your-api-key"
# Call the LLM model
def call_llm_api(user_input):
    # Read system prompt content from a file
    with open("SYSTEM_PROMPT", "r") as file:
        system_prompt = file.read().strip()

    payload = {
        "model": "localmind-pro",  # Replace with your actual model version
        "messages": [
            {"role": "system", "content": system_prompt},  # Use the content from the SYSTEM_PROMPT file
            {"role": "user", "content": user_input}
        ]
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {LLM_API_KEY}"
    }
    response = requests.post(LLM_BASE_URL, json=payload, headers=headers)
    return response.json()  # Returns the API response as a Python dictionary

# Function to find and validate JSON in markdown code block
def extract_and_validate_json(text):
    # Regex to find markdown code blocks
    matches = re.findall(r"```(.*?)```", text, re.DOTALL)
    for match in matches:
        try:
            # Attempt to parse the code block as JSON
            parsed_json = json.loads(match)
            return True, parsed_json  # Return True and the parsed JSON if successful
        except json.JSONDecodeError:
            continue  # If it's not valid JSON, continue to check other matches
    return False, None  # Return False if no valid JSON code block was found

@app.route('/function_call', methods=['POST'])
def function_call():
    request_data = request.json
    user_input = request_data.get('text')

    if not user_input:
        return jsonify({"error": "No text provided"}), 400

    # Call the LLM API
    llm_response = call_llm_api(user_input)

    # Attempt to extract the message from the LLM response
    try:
        llm_message = llm_response['choices'][0]['message']['content']
    except (KeyError, IndexError, TypeError):
        return jsonify({"error": "Invalid response structure from LLM"}), 500

    # Check if the LLM message contains a valid JSON in a markdown code block
    json_found, json_data = extract_and_validate_json(llm_message)

    response_data = {
        "response": llm_message,
        "valid_json_found": json_found,
        "json_data": json_data,
        "timestamp": datetime.now().isoformat()  # Add the current timestamp
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
