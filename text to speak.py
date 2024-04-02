import pyttsx3
txt=pyttsx3.init()
while True:
    ans=input("what do you want to say? ")
    txt.say(ans)
    txt.runAndWait()
    c=input("do you want to test it again?(yes or no)")
    if c=='no':
        break