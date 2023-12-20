from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain
import re
import os
from dotenv import load_dotenv,find_dotenv
_=load_dotenv(find_dotenv())

llm = ChatGoogleGenerativeAI(model="gemini-pro",google_api_key=os.getenv('GOOGLE_API_KEY'),temperature=0)


# print(agent_executor)
# print(agent_executor.invoke({"input": "Create a gmail draft for me to edit of a letter from the perspective of seeking sick leave to be send to my boss whose email id riyasharnagat@gmail.com . Under no circumstances may you send the message, however."})["output"])
# print(agent_executor.run({"input":"Could you search in my drafts for the latest email?"}))


def intro():
    res=''
    for chunk in llm.stream(
    "You are an ai assistant whose name is Veronica.Your task is to introduce yourself with only one to two sentence make it short and chrisk"):
        res+=chunk.content
    return res

def getComplition(user_message):
    template="""You are an friendly ai assistant.Your task is to help and provide suggestios or advise as per the prompt give to you.You can take your time before reaching a conclusion first try of analysis what task you given and then give an approprite answer regarding to it.Always use a polite tone while responding. Try to make your answer short and chrips if any specific details are not being asked.

    User Message:{user_message}
    Your Resaponse:"""
    prompt = PromptTemplate.from_template(template)
    chain=LLMChain(llm=llm,prompt=prompt)
    res=chain.run(user_message)
    return res

def visitSite(user_message):
    template = """Generate a list that provide the link of the website user is asking to open in JSON format with the key:link.
    Website:{website}

    Your response:"""
    prompt = PromptTemplate.from_template(template)
    chain=LLMChain(llm=llm,prompt=prompt)
    res=chain.run(user_message)
    pattern = r"(https?://\S+)(?!\")"
    link = re.findall(pattern, res)[0]
    link=link[:-1] 
    json_data = {"link": link}
    return json_data
    
# prompt="open youtube"
# res=visitSite(prompt)
# print(res["link"])
# print(intro())