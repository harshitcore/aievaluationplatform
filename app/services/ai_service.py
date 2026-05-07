import os
from dotenv import load_dotenv
from openai import OpenAI

# Load the .env file so the system can find OPENAI_API_KEY
load_dotenv()

# Provide a fallback string so the app doesn't crash on boot if the key is missing
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "dummy-key-to-prevent-crash"))

class RealAIService:
    @staticmethod
    def generate_responses(prompt):
        # Model A 
        resp_a = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
           )
           
           # Model B 
        resp_b = client.chat.completions.create(
               model="gpt-4",
               messages=[{"role": "user", "content": prompt}]
           )

        return {
               'model_a': resp_a.choices[0].message.content,
               'model_b': resp_b.choices[0].message.content
           }