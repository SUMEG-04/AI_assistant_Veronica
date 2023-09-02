import win32com.client
import speech_recognition as sr
import webbrowser
from openai_script import *
speaker=win32com.client.Dispatch('SAPI.SpVoice')
voices = speaker.GetVoices()
female_voice = voices.Item(1)
speaker.Voice = female_voice

def takeinp():
    r=sr.Recognizer()
    try:
        with sr.Microphone() as mic:
            r.pause_threshold=1
            audio=r.listen(mic)
            text=r.recognize_google(audio,language='en-in')
            text=text.lower()
            return text
    except Exception as e:
        return "Didn't hear clearly"

if __name__=="__main__":
    s=intro()
    speaker.Speak(s)
    while True:
        print("Listening....")
        text=takeinp()
        print(text)
        if(text!="Didn't hear clearly"):
            if f"open" in text:
                res=visitSite(prompt=text)
                site=res[12:(len(res)-4)]
                speaker.Speak(f"Opening {site} sir..")
                webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open_new(res)
            else:
                res=getComplition(prompt=text)
                print(res)
                speaker.Speak(res)
        else:
            speaker.Speak(text)