import requests

from init.tokens import get_hf_token

def main():

	hf_token = get_hf_token()

	API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-v0.1"
	headers = {"Authorization": f"Bearer {hf_token}"}

	def query(payload):
		response = requests.post(API_URL, headers=headers, json=payload)
		return response.json()
		
	output = query({
		"inputs": "What is going out there?",
	})

	print(output)

if __name__ == "__main__":
    main()