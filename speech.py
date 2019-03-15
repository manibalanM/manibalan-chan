from gtts import gTTS
import pyglet
import speech_recognition as sr

def voice(cont):
    files = gTTS(text=cont,lang="en")
    filename="audio.mp3"
    files.save(filename)
    music = pyglet.resource.media(filename,streaming = False)
    music.play()

def speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        
    try:
        s = r.recognize_google(audio)
        print ("Done")
        print("your speech: "+s)
        return s
    except Exception as e:
        print("Exception: "+str(e))


def song():
    filename="father.mp3"
    music = pyglet.resource.media(filename,streaming = False)
    music.play()

if __name__ == "__main__":
    song()
