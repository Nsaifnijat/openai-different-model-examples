
import config

from openai import OpenAI
import os

# Initialize the OpenAI client
client = OpenAI(api_key=config.open_ai_key)

"""
# Ensure your API key is set as an environment variable
if not os.getenv("OPENAI_API_KEY"):
    print("Please set your OPENAI_API_KEY as an environment variable.")
    exit(1)
"""
def generate_response(messages):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # You can change this to "gpt-4" if you have access
            messages=messages
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {str(e)}"

def main():
    conversation = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]
    
    print("Welcome! Start chatting with the AI. Type 'quit' to exit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break
        
        conversation.append({"role": "user", "content": user_input})
        
        ai_response = generate_response(conversation)
        print("AI:", ai_response)
        
        conversation.append({"role": "assistant", "content": ai_response})

if __name__ == "__main__":
    main()