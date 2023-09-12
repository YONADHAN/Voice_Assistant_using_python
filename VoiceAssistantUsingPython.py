import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Not understood")
            return "error"  # Return a string instead of None

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice",voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()

if __name__ =='__main__':

    while True:
        temp = sptext().lower()
        if temp == "error":  # Handle the "error" case
            speechtx(" ")
        elif temp == "elephant":
            data1 = sptext().lower()

            if "error" in data1:
                speechtx(" ")
            elif "your name" in data1:
                name = "My name is peter."
                speechtx(name)
            elif "old are you" in data1:
                age = "I am 2 years old."
                speechtx(age)
            elif 'now time' in data1:
                time = datetime.datetime.now().strftime("%I:%M %p")
                speechtx(time)
            elif 'yahoo' in data1:
                webbrowser.open('https://www.yahoo.com/')
            elif 'duckduckgo' in data1:
                webbrowser.open('https://duckduckgo.com/')
            elif 'godaddy' in data1:
                webbrowser.open('https://www.godaddy.com/')
            elif 'webmd' in data1:
                webbrowser.open('https://www.webmd.com/')
            elif 'healthline' in data1:
                webbrowser.open('https://www.healthline.com/')
            elif 'mayo clinic' in data1:
                webbrowser.open('https://www.mayoclinic.org/')
            elif 'dictionary.com' in data1:
                webbrowser.open('https://www.dictionary.com/')
            elif 'thesaurus.com' in data1:
                webbrowser.open('https://www.thesaurus.com/')
            elif 'adobe' in data1:
                webbrowser.open('https://www.adobe.com/')
            elif 'canva' in data1:
                webbrowser.open('https://www.canva.com/')
            elif 'pixabay' in data1:
                webbrowser.open('https://pixabay.com/')
            elif 'pexels' in data1:
                webbrowser.open('https://www.pexels.com/')
            elif 'unsplash' in data1:
                webbrowser.open('https://unsplash.com/')
            elif 'behance' in data1:
                webbrowser.open('https://www.behance.net/')
            elif 'dribbble' in data1:
                webbrowser.open('https://dribbble.com/')
            elif 'deviantart' in data1:
                webbrowser.open('https://www.deviantart.com/')
            elif 'pinterest' in data1:
                webbrowser.open('https://www.pinterest.com/')
            elif 'fiverr' in data1:
                webbrowser.open('https://www.fiverr.com/')
            elif 'upwork' in data1:
                webbrowser.open('https://www.upwork.com/')
            elif 'freelancer' in data1:
                webbrowser.open('https://www.freelancer.com/')
            elif 'indeed' in data1:
                webbrowser.open('https://www.indeed.com/')
            elif 'glassdoor' in data1:
                webbrowser.open('https://www.glassdoor.com/')
            elif 'monster' in data1:
                webbrowser.open('https://www.monster.com/')
            elif 'zillow' in data1:
                webbrowser.open('https://www.zillow.com/')
            elif 'trulia' in data1:
                webbrowser.open('https://www.trulia.com/')
            elif 'realtor' in data1:
                webbrowser.open('https://www.realtor.com/')
            elif 'homeadvisor' in data1:
                webbrowser.open('https://www.homeadvisor.com/')

            elif 'better business bureau' in data1:
                webbrowser.open('https://www.bbb.org/')

            elif "joke" in data1:
                joke_1 = pyjokes.get_joke(language="en", category="neutral")
                print(joke_1)
                speechtx(joke_1)

            elif 'song' in data1:
                add = "C:/Users/Yonadhan MM/Music/JWLibrary"
                listsong = os.listdir(add)
                print(listsong)
                os.startfile(os.path.join(add, listsong[0]))

            elif 'exit' in data1:
                speechtx("Thankyou")
                break