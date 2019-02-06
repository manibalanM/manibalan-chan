from gtts import gTTS
import pyglet

def voice(cont):
    files = gTTS(text=cont,lang="en")
    filename="audio.mp3"
    files.save(filename)
    music = pyglet.resource.media(filename,streaming = False)
    music.play()
voice("how are you")
