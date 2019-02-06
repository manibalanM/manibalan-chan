import speech_recognition as sr

r = sr.Recognizer()



with sr.Microphone() as source:
    print ("say something...!")
    audio = r.listen(source)

try:
    s = r.recognize_google(audio)
    print ("Done")
    print("Text: "+s)
except Exception as e:
    print("Exception: "+str(e))
