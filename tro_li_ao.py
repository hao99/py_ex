import pyttsx3
import speech_recognition
from datetime import date, datetime

robot_mouth = pyttsx3.init()
robot_ear = speech_recognition.Recognizer()
while True:
    with speech_recognition.Microphone() as mic:
        print("Robot: I'm listening!")
        audio = robot_ear.listen(mic)
    try:
        you = robot_ear.recognize_google(audio)
    except:
        you = ""
    print("You: "+you)
    if you == "":
        robot_brain = "I can't hear what you say"
    elif "hello" in you:
        robot_brain = "Hello Phung Hao!"
    elif "today" in you:
        today = date.today()
        robot_brain = today.strftime("%B %d, %y")
    elif "time" in you:
        now = datetime.now()
        robot_brain = now.strftime("%H hours %M minutes %S seconds")
    elif you == "president":
        robot_brain = "Bidennnn"
    elif "thank you" in you:
        robot_brain = "You are welcome!"
    elif "ok" in you:
        robot_brain = "ngu thi chet con me may di, khoc loc cai dau buoi!"
    elif "bye" in you:
        robot_brain = "bye"
        print("Robot: " + robot_brain)
        volume = robot_mouth.getProperty('volume')
        voices = robot_mouth.getProperty('voices')
        robot_mouth.setProperty('volume', 1.0)
        robot_mouth.setProperty('voice', voices[1].id)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    else:
        robot_brain = "I'm fine thank you and you"
    print("Robot: "+robot_brain)

    volume = robot_mouth.getProperty('volume')
    voices = robot_mouth.getProperty('voices')
    robot_mouth.setProperty('volume',1.0)
    robot_mouth.setProperty('voice', voices[1].id)
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()