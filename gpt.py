#Making own gpt using python..

import openai
openai.api_key = 'Enter your OpenAI API key here'
message = [{"role": "system", 
            "content":
    "You are a helpful assistant."},]

while True:
    message= input("User: ")
    if message:
        message.append({"role": "User",
                        "content": message}
                       )
    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message
    )
    
    Replay= chat.choices[0].message.content
    print(f"ChatGpt: {Replay} ", ) 
    message.append({"role": "assistant",
                        "content": Replay}
                       )   
