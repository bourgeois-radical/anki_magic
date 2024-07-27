import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

def get_hf_token():
    # Access the HF_ACCESS_KEY variable

    hf_access_key = os.getenv('HF_TOKEN')
    if hf_access_key:
        print('Hugging Face access key has been loaded')
        return hf_access_key
    else:
        print('Hugging Face access key not found')
        exit(1)  # Exit with a status code to indicate an error

# Example usage
if __name__ == "__main__":
    hf_access_key = get_hf_token()
    print(f'Your Hugging Face Access Key is: {hf_access_key}')