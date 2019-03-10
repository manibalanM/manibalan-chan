import bs4
import requests
import speech


def google(s):
    
    url = 'https://www.google.com/search?q='+s
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text,'html.parser')
    x=0
    for i in soup.find_all("span",class_ ="st"):
        print (i.getText())
        x+=1
        if x==2:
            break


def wiki(a):
    url = 'https://en.wikipedia.org/wiki/'+a
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text,'lxml')
    x=0
    for i in soup.find_all('p'):
        print (i.getText())
        x+=1
        if x==2:
            break
    

if __name__ == "__main__":
    print("speech to search : ")
    s = speech.speech()
    google(s)
