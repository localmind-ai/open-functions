import requests
import json

def main():
    print("Welcome to the Localmind CLI Interface for Function Calling.")
    print("Type 'exit' to leave the CLI.")

    # Define your FastAPI endpoint
    api_endpoint = "http://localhost:8000/function_call"  # Adjust the URL if your FastAPI app is hosted elsewhere

    while True:
        # Get user input
        user_input = input("Enter your prompt: ")
        if user_input.lower() == 'exit':
            print("Exiting Localmind Function Calling CLI.")
            break

        # Prepare the payload for the API request
        payload = {
            "text": user_input
        }
        headers = {
            "Content-Type": "application/json"
        }

        # Send the request to the FastAPI application
        try:
            response = requests.post(api_endpoint, json=payload, headers=headers)
            response_data = response.json()

            # Check if the response contains valid JSON in a markdown code block
            if response_data.get('valid_json_found'):
                print("Valid JSON found in response:")
                print(json.dumps(response_data['json_data'], indent=2))
            else:
                print("Response:")
                print(response_data['response'])

            print("Timestamp:", response_data['timestamp'])

        except requests.RequestException as e:
            print(f"Error connecting to the API: {e}")

if __name__ == "__main__":
    main()
