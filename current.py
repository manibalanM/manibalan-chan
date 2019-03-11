import speech
import scrap

print ("say what to search")
s = speech.speech()

a=s
if 'who' in s or'what' in s or'when' in s:
    scrap.google(a)
elif 'about'  in s or'About' in s:
    
    a = a[6:]
    scrap.wiki(a)
else:
    b = scrap.wikipedia(a)
    if (b<600):
        scrap.wiki(a)
    else:
        scrap.google(a)
