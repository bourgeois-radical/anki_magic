import os
from dotenv import load_dotenv

# Load the environment variables from the .secret file
load_dotenv('.secret')

# Access the HF_TOKEN variable
hf_token = os.getenv('HF_TOKEN')
if hf_token:
    print('HF_TOKEN has been loaded')
else:
    print('HF_TOKEN not found')