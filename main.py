import smtplib  #  Simple Mail Transfer Protocol
import speech_recognition as sr #speech_recognition is named as sr
import pyttsx3 # it is python text to speech
from email.message import EmailMessage# to structure the email message

listener = sr.Recognizer()# this functions recognizes whatever we are saying
engine = pyttsx3.init()# this initialises python text to speech

def talk(text):
    engine.say(text)# it converts the text to audio
    engine.runAndWait()# it runs and wait

def get_info():
    try:
        with sr.Microphone() as source: #sr.Microphone is named as source and it listens to the microphone
            print('listening...')
            voice = listener.listen(source)# listener listens whatever is coming from the source
            info = listener.recognize_google(voice) # convert the audio to text
            print(info)
            return info.lower()

    except:
        pass#if the program enters except it will pass and go back to try

def send_mail(receiver,subject,message):
    server = smtplib.SMTP('smtp.gmail.com', 587)# declaring a variable and calling a function in smtp lib sendig the port no
    server.starttls() # transport layer security
    server.login('gauthammudaliar13@gmail.com', 'Enter Your Password')
    email = EmailMessage()
    email['From'] = 'gauthammudaliar13@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    'Ambani': 'ambani@gmail.com',
    'virat': 'vkohle@gmail.com'
}

def get_email_info():
    talk('To Whom you want to send email')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('what is the subject of the email')
    subject = get_info()
    talk('tell me the text in your email')
    message = get_info()
    send_mail(receiver, subject, message)
    talk('do you want to send more email?')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()
    else:
        exit


get_email_info()
