import os
import openai
from dotenv import load_dotenv,find_dotenv
_=load_dotenv(find_dotenv())
openai.api_key=os.getenv('OPENAI_API_KEY')

def intro():
    model="gpt-3.5-turbo"
    messages = [{"role": "user", "content": "You are an ai assistant whose name is Veronica.Your task is to introduce yourself."}]
    response = openai.ChatCompletion.create(
        model=model,
        max_tokens=30,
        messages=messages,
        temperature=1,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].message["content"]

def getComplition(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
        {
          "role": "system",
          "content": "You are an friendly ai assistant.Your task is to help and provide suggestios or advise as per the prompt give to you.You can take your time before reaching a conclusion first try of analysis what task you given and then give an approprite answer regarding to it.Always use a polite tone while responding.\
            If user is asking about opening a website generate a list that provide the link to the website in JSON format with the key:link, with no other text."
        },
        {
            "role": "user",
            "content": f"{prompt}"
        },
        {
            "role": "assistant",
            "content": ""}
        ],
        temperature=1,
        max_tokens=80,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].message["content"]

def visitSite(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
        {
          "role": "system",
          "content": "Generate a list that provide the link of the website user is asking to open in JSON format with the key:link."
        },
        {
            "role": "user",
            "content": f"{prompt}"
        },
        {
            "role": "assistant",
            "content": ""}
        ],
        temperature=1,
        max_tokens=50,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    res=response.choices[0].message["content"]
    return res

prompt="open google"
res=visitSite(prompt)
