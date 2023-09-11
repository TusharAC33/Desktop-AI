import sys
import pyttsx3
import speech_recognition as sr
import datetime
import os
from PyQt5.QtWidgets import QApplication

import david

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 200)


def start_listening(self):
    self.response_label.setText('Listening...')
    self.response_label.repaint()
    while True:
        query = self.take_command().lower()
        self.tasks(query)


def take_command(self):
    with sr.Microphone() as source:
        print("Listening...")
        self.response_label.setText("Listening...")
        self.response_label.repaint()
        audio = self.recognizer.listen(source)

        try:
            print("Recognizing...")
            self.response_label.setText("Recognizing...")
            self.response_label.repaint()
            query = self.recognizer.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
            self.response_label.setText(f"User said: {query}")
            self.response_label.repaint()
        except Exception as e:
            print(e)
            self.response_label.setText("Can you repeat what you said")
            self.response_label.repaint()
            query = "none"

        return query


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour <= 12:
        speak("Good morning")
    elif 12 <= hour <= 18:
        speak("Good Afternoon")
    else:
        speak("Good evening")
    speak("Hello, My name is Hazel, Iam your Assistant, How can I help you")


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        speak("Can you repeat what you said")
        return "none"
    return query


# def take_command_hin():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening")
#         audio = r.listen(source)
#     try:
#         print("Recognizing...")
#         query = r.recognize_google(audio, language='hi')
#         print(f"User said: {query}\n")
#
#     except Exception as e:
#         print(e)
#         speak("Can you repeat what you said")
#         return "none"
#     return query


def tasks(query):

    if 'time' in query:
        current_time = datetime.datetime.now().strftime('%H:%M')
        speak(f"The time is {current_time}.")


    elif 'date' in query:
            current_date = datetime.datetime.now().strftime('%Y-%m-%d')
            speak(f"Today's date is {current_date}.")


    elif 'search' in query or 'google search' in query:
        Qquery=query.replace("search", "")
        Query=query.replace("google search", "")
        from features import googlesearch
        if "search" in query:
            googlesearch(Qquery)
        else:
            googlesearch(Query)


    elif 'from youtube' in query:
        from features import youtube
        youtube(query)

    elif 'alarm' in query:
        from features import alarm
        speak("enter the time")
        alarm_time = input("Enter the alarm time (HH:MM format): ")
        alarm(alarm_time)


    elif 'Chrome' in query or 'Browser' in query:
        from features import chrome_auto
        query.replace("Chrome", "")
        chrome_auto(query)


    elif 'my location' in query:
        from features import my_location
        my_location()


    elif 'where is' in query:
        place = query.replace("where is", "")
        from features import map
        map(place)

    elif 'write a note' in query or 'make a note' in query:
        from features import notepad
        notepad()

    elif 'close the note' in query:
        from features import close_note
        close_note()

    elif 'tell me a joke' in query:
        from features import jokes
        jokes()



    elif 'weather in' in query or 'temperature in' in query:
        from features import get_weather
        from features import speakWeather
        city_name = query.replace("weather in ", "").replace("temperature in ", "")
        weather_info = get_weather(city_name)
        speakWeather(weather_info, city_name)


    elif 'news' in query:
        from features import news
        news()


    elif 'launch' in query:
        app_name = query.replace('launch', '').strip()
        from features import launch_application
        launch_application(app_name)

    elif "ip address" in query:
        from features import getip
        getip()

    elif 'take a screenshot' in query:
        from features import take_screenshot
        take_screenshot()
        speak("Screenshot taken and saved.")

    elif 'what is' in query or 'who' in query or 'where' in query or 'how' in query or 'can you' in query or 'do you' in query:
        from features import generic_question_answer
        answer = generic_question_answer(query)
        print(answer)
        speak(answer)

    elif 'song please' in query or 'play some songs' in query:
        speak("Which song do you want me to play")
        song = take_command()
        from features import playsong
        playsong(song)
        exit()


    elif "shutdown the system" in query:
        speak("Are You sure you want to shutdown")
        shutdown = input("Do you wish to shutdown your computer? (yes/no)")
        if shutdown == "yes":
            os.system("shutdown /s /t 1")

        elif shutdown == "no":
            exit()


    else:
        print("none")


if __name__ == "__main__":
    wishMe()
    '''Gui_App = QApplication(sys.argv)
    window = david.Gui_Start()
    window.show()'''

    while True:
        query = take_command().lower()
        if "see you later" in query or "take some rest" in query:
            speak("Ok sir , You can me call anytime")
            speak("going to sleep")
            speak("bye,bye")
            break
        tasks(query)

    '''sys.exit(Gui_App.exec_())'''




