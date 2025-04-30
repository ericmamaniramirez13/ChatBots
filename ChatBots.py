import os;
from dotenv import load_dotenv;
from google import genai;

load_dotenv()
try:
    api_key = os.environ.get("GEMINI_API_KEY")
except KeyError:
    print("Please set the GEMINI_API_KEY environment variable with your API key.")

with open("InitialPrompt.txt", "r") as file:
    initial_prompt = file.read()

client = genai.Client(api_key = api_key)
conversation_history = [{"role": "user", "parts": [{"text": initial_prompt}]}]
def chat_with_gemini(prompt):
    user_turn = {"role": "user", "parts": [{"text": prompt}]}
    conversation_history.append(user_turn)
    response = client.models.generate_content(
    model="gemini-2.0-flash-lite", contents=conversation_history
)
    response_text =  response.text
    model_turn = {"role":"model", "parts": [{"text": response_text}]}
    conversation_history.append(model_turn)
    return response_text
print(chat_with_gemini("why should i hire this candidate?"))
print(chat_with_gemini("how this candidate stands out from others"))