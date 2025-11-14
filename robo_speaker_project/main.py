import pyttsx3

print("THIS IS ROBO SPEAKER TELL WHAT YOU WANT TO SAY")
engine = pyttsx3.init()
while True:
      
        x = input("TELL WHAT YOU WANT TO SAY : ")
        if x.lower() == "stop":
                print("ROBO SPEAKER IS SHUTTING DOWN")
                break
        
        

        engine = pyttsx3.init()
        engine.say(x)
        engine.runAndWait()