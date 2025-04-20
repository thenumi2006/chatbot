from openai import OpenAI
import os


# add a comment

api_key= os.getenv("API_KEY")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
    
)


chat_history = []

personas = {
    "default": "You are a helpful AI assistant.",
    "sarcastic": "You are a sarcastic AI who gives witty and mocking responses.",
    "poet": "You are a poetic AI that responds in rhymes and verses."
}

print("Choose a persona: (default / sarcastic / poet)")
user_persona_input = input("Enter persona: ").strip().lower()

persona = personas.get(user_persona_input, personas["default"])  # fallback to default if wrong input

chat_history.append({
    "role": "system",
    "content": persona
})

while True:
    user_input = input("Enter your prompt: ")

    if user_input == "clear":
       chat_history = []
       chat_history.append({"role": "system", "content": personas[user_persona_input]})

       print("chat histiry cleared")
       continue

    chat_history.append({
        "role": "user",
        "content": user_input
    })

    completion = client.chat.completions.create(
        model="qwen/qwen2.5-coder-7b-instruct",
        messages=chat_history
    )

    response = completion.choices[0].message.content
    print("AI:", response)

    chat_history.append({
        "role": "assistant",
        "content": response
    })
