import requests
import json
from win32com.client import Dispatch
def speak(Str):
    speak= Dispatch("SAPI.SpVoice")
    speak.Speak(Str)

if __name__ == '__main__':
    speak("News For Today...")
    url="http://newsapi.org/v2/everything?q=tesla&from=2021-01-20&sortBy=publishedAt&apiKey=3911af7dd20d4c61951ac3fdf3cb783a"
    news= requests.get(url).text
    news_dict=json.loads(news)
    artic=news_dict['articles']
    for article in artic:
        speak(article['title'])
        speak("The next news is ...Listen carefullu")
    speak("Thanks for Listening")