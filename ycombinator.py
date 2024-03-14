import requests
import pyttsx3
import time


def talk(command):
    engine = pyttsx3.init()
    voice = engine.getProperty("voices")
    engine.setProperty("voice", voice[1].id)
    engine.say(command)
    engine.runAndWait()


api = "https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty"

jsonapi = requests.get(api)
jsonapi = jsonapi.json()
n = len(jsonapi)
while True:
    n -=1
    postapi = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{jsonapi[n]}.json?print=pretty")
    postapi = postapi.json()
    print(postapi)
    talk(postapi['title'])
    print("\n")
    time.sleep(2)
    if n == 0 :
        break
