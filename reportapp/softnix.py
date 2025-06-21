import os
import requests
import urllib3
# Disable SSL warnings
urllib3.disable_warnings()

def call_api(context, question):
    """
    Calls the Softnix API to get a response.
    """
    # Ensure the API key is set
    key = os.getenv("API_KEY")
    if not key:
        print("API key is not set.")
        return

    url = "https://genai.softnix.ai/external/api/completion-messages"
    payload = {
        "inputs": {"context": context, "question": question},
        "citation": True,
        "response_mode": "blocking",
    }
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {key}"}
    try:
        response = requests.post(url, 
                                 json=payload, 
                                 headers=headers, 
                                 timeout=30,
                                 verify=False)
        response.raise_for_status()  # Raise an error for bad responses
    except requests.exceptions.RequestException as e:
        print(f"Error calling API: {e}")
        return
    print("API Response:")
    print(response.json())
    # Return the JSON response
    if response.status_code != 200:
        print(f"Error: {response.status_code} - {response.text}")
        return None
    return response.json()
