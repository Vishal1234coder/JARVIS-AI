import pyttsx3
import speech_recognition as sr

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 200)  # Adjust the speed (rate) of speech
    engine.setProperty('volume', 1)  # Adjust the volume

    voices = engine.getProperty('voices')
    # You might need to identify the index of a robotic voice within available voices
    # Check the voices available on your system and select a suitable one
    engine.setProperty('voice', voices[0].id)  # Adjust the voice (select a robotic voice)

    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1.5
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-us')

    except Exception as e:
        print(e)
        return ""
    return query


pass

if __name__ == "__main__":
    speak("Hello, I am Your Virtual Assistant. How Can I Assist You Today?")
    query = take_command()
    print(query)
    speak(query)
