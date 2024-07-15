import requests

API_KEY = 'YOUR_OPENAI_API_KEY'
URL = 'https://api.openai.com/v1/engines/davinci-codex/completions'

def get_summary(text):
    try:
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {API_KEY}'
        }
        summary_prompt = f"Summarize this text: {text}"
        summary_data = {
            'model': 'gpt-3.5-turbo-instruct',
            'prompt': summary_prompt,
            'max_tokens': 100,
            'temperature': 0
        }
        
        summary_response = requests.post(URL, headers=headers, json=summary_data)
        
        # Check for HTTP errors
        summary_response.raise_for_status()
        
        # Parse response JSON
        response_json = summary_response.json()
        
        # Check if 'choices' is in response and not empty
        if 'choices' in response_json and response_json['choices']:
            summary = response_json['choices'][0]['text']
            return summary.strip()
        else:
            print(f"Unexpected response format: {response_json}")
            return None
    
    except requests.exceptions.RequestException as e:
        print(f"Error making request to OpenAI API: {e}")
        return None
    except (KeyError, ValueError) as e:
        print(f"Error parsing response from OpenAI API: {e}")
        return None
