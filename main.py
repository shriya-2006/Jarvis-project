import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os



recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "YOUR_NEWS_API_KEY""

def speak_old(text):
    engine.say(text)
    engine.runAndWait()


def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3') 

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3") 

def aiProcess(command):
    client = OpenAI(
        api_key="YOUR_GROQ_API_KEY",
        base_url="https://api.groq.com/openai/v1"

    )

    completion = client.chat.completions.create(
    model="llama3-70b-8192",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
        {"role": "user", "content": command}
    ]
    )

    return completion.choices[0].message.content


def processCommand(c):
    c = c.lower().strip()
    print("Recognized command:", c)
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")   
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")   
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    elif any(word in c for word in ["news", "headlines", "tell me news"]):
        speak("Fetching the latest news for you.")
        r = r = requests.get(f"https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={newsapi}")

        print("News API status code:", r.status_code)
        if r.status_code == 200:
            #parse the JSON response
            data = r.json()

            #Extract the articles
            articles = data.get('articles', [])
            print("Number of articles:", len(articles))

            #headlines
            for article in articles:
                title = article.get("title", "No title available")
                print("Speaking headline:", title)
                speak(article['title'])
    else:
        #Let OpenAi handle the request
        response = aiProcess(c)
        print("Jarvis:", response)
        speak(response)






if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
        
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=1)
                print("Listening...")
                audio = r.listen(source, timeout=3, phrase_time_limit=4)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Ya")
                #Listen for command
                with sr.Microphone() as source:
                    recognizer.adjust_for_ambient_noise(source, duration=1)
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)


        except Exception as e:
            print("Error; {0}".format(e))

        
        

    
