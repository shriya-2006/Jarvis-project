 Jarvis - Your Personal Voice Assistant
Jarvis is a Python-based virtual voice assistant that listens for a wake word, recognizes voice commands, and performs tasks like opening websites, playing music, fetching news, or answering general queries using an AI model.

FEATURES
Wake-word activation ("Jarvis")
Opens popular websites via voice
Plays music from a predefined library
Fetches live news from BBC using NewsAPI
Handles general conversation using Groq API LLaMA 3 model
Converts text to speech using gTTS and plays it using Pygame

Technologies Used
speech_recognition – for recognizing voice commands
pyttsx3 & gTTS – text-to-speech
pygame – to play MP3 responses
webbrowser – to open URLs
requests – for fetching news via NewsAPI
Groq API LLaMA 3 – to handle AI chat responses
Python – the main programming language

Jarvis-project/
├── main.py                  # Main voice assistant script
├── musicLibrary.py          # Dictionary linking music names to URLs
├── README.md                # Project info and usage
└── requirements.txt         # List of Python dependencies



