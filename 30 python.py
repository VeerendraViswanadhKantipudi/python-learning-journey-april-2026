from gtts import gTTS
import speech_recognition as sr
import playsound
from time import ctime
import os
import smtplib
import webbrowser
import uuid  

# to make sure it listens
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:  
        print("Start talking")
        audio = r.listen(source, phrase_time_limit=5)  
    data = ""
    # exception handling
    try:
        data = r.recognize_google(audio, language='en-US')  
        print("You said :" + data)
    except sr.UnknownValueError:
        print("I cannot hear you")
    except sr.RequestError as e:
        print("request Failed")
    return data

# to respond back with audio
def respond(String):
    print(String)
    tts = gTTS(text=String, lang='en-US')
    filename = "Speech%s.mp3" % str(uuid.uuid4())
    tts.save(filename)
    playsound.playsound(filename)  
    os.remove(filename)

# virtual Assistant actions
def virtual_assistant(data):
    """give your actions"""
    listening = True
    
    if "how are you" in data:
        respond("Good and doing well")
    if "time" in data:
        respond(ctime())
    if "open google" in data.casefold():
        url = "https://www.google.com/"
        webbrowser.open(url)
        respond("Success")
    if "locate" in data:
        webbrowser.open('https://www.google.com/maps/search/' + data.replace("locate", ""))
        respond("Located {}".format(data.replace("locate", "")))  
    if "email" in data:
        respond("whom should i send email to?")
        to = listen().lower()
        edict = {"nani": "nani68395@gmail.com"} 
        toaddr = edict[to]
        respond("what is the subject?")  
        subject = listen()
        respond("What should i tell that person?")  
        message = listen()
        content = 'Subject: {}\n\n{}'.format(subject, message)  
        # init gmail SMTP
        mail = smtplib.SMTP('smtp.gmail.com', 587)  
        # identify the server
        mail.ehlo()  
        mail.starttls()  
        # login
        mail.login('kantipudiveerendra69@gmail.com', "ddos ktdg squb hqaa")  
        mail.sendmail('kantipudiveerendra69@gmail.com', toaddr, content)  
        mail.close()
        respond('Email Sent')
    if "stop" in data:
        listening = False
        print("Listening Stopped")
        respond("Okay done take care......")
    
    return listening

# Main execution
respond("Hey Veerendra how are you")
listening = True
while listening == True:
    data = listen()
    listening = virtual_assistant(data)
