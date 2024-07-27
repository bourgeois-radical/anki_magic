import os
from dotenv import load_dotenv
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load the environment variables from the .secret file
load_dotenv('.secret')

# Access the HF_TOKEN variable
hf_token = os.getenv('HF_TOKEN')
if hf_token:
    print(f"HF_TOKEN: {hf_token}")
else:
    print("HF_TOKEN not found")


tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-v0.1", token=hf_token)
model = AutoModelForCausalLM.from_pretrained("mistralai/Mistral-7B-v0.1")