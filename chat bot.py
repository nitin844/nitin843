from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pp
import speech_recognition as s
import threading
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.logic import LogicAdapter










engine=pp.init()
voices=engine.getProperty('voices')
print(voices)

engine.setProperty('voice',voices[0].id)

def speak(WORD):
    engine.say(WORD)
    engine.runAndWait()

Sam=ChatBot("My Sam", 
            storage_adapter='chatterbot.storage.SQLStorageAdapter',
            
            logic_adapters=[
                  'chatterbot.logic.MathematicalEvaluation',
                  'chatterbot.logic.BestMatch',
                   
 
                 
        
    ],
    database_uri='sqlite:///database.sqlite3',
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace'
    ]
                 

    

  )

  
convo = [
    'hello sir',
    'sir',
    'hi there !',
    'what is your name ?',
    'my name is Sam , i am created by NKB'
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
    'i am doing great these days',
    'how are you',
    'thank you',
    'in which city you live ?',
    'i live in Ghaziabad ',
    'in which language you talk',
    'i mostly talk in english',
    'what is your age',
    'my age is 19',
    'what is famous in your city',
    'parks,temples,street food,mostly the beauty',
    'are you single',
    'ya i am single?',
    'do you have any boyfriend',
    'ya ! i have',
    'do you have any girlfriend',
    'yes',
    'girlfriend name',
    'alexis',
    'want to mingle??',
    'perhaps',
    'what are your hobby',
    'cooking, sketching, dancing, coding',
    'tune gali kese di, fuck you',
    'pagal he kya',
    'tu pagal tera baap pagal',
    'your girlfiend name',
    'aaloo',
    'How are you?',
    'I am good.',
    'That is good to hear.',
    'Thank you',
    'You are welcome.',
     "Greetings!",
      "How are you?",
    "I am good.",
    "That is good to hear.",
     'How can I help you?',
    'I want to create a chat bot',
    'Have you read the documentation?',
    'No, I have not',
    ' your father name ?',
    'Nkb',
    ' your uncle name',
    'saurabh maurya',
    'your mother name',
    'aaloo',
    'your girlfriend name',
    'Alka Bodha',
    'your grandfather name',
    '',






]



trainer=ListTrainer(Sam)

trainer.train(convo)



answer=Sam.get_response("what is your name?")
print(answer)



print("Talk to Sam")










class MyLogicAdapter(LogicAdapter):

 def __init__(self, chatbot, **kwargs):
     super().__init__(chatbot, **kwargs)

def can_process(self, statement):
        return True

def process(self, input_statement, additional_response_selection_parameters):
        import random

        
        confidence = random.uniform(0, 1)

        
        selected_statement = input_statement
        selected_statement.confidence = confidence

        return selected_statement



    

main = Tk()

main.geometry("400x580")
main.title("its Sam")
img = PhotoImage(file="C:/Users/Nkb/Downloads/animated-frog-image-0015.gif")
photoL = Label(main, image=img)

photoL.pack(pady=5)



def takeQuery():
    sr=s.Recognizer()
    sr.pause_threshold=1
    print(' Sam is listening try to speak')
    with s.Microphone() as m:
        try:
            audio=sr.listen(m)  
            query=sr.recognize_google(audio,language='eng-in')
            print(query)
            textF.delete(0,END)
            textF.insert(0,query)
            Ask_from_Sam()
        except Exception as e:
            print(e)    
            print("not recognized")


def Ask_from_Sam():
    query = textF.get()
    answer_from_Sam = Sam.get_response(query)
    msgs.insert(END, 'you : ' + query)
    print(type(answer_from_Sam))
    msgs.insert(END, 'Sam : ' + str(answer_from_Sam))
    speak(answer_from_Sam)
    textF.delete(0, END)
    msgs.yview(END)

    query = textF.get()
    answer_from_Sam = Sam.get_response(query)
    msgs.insert(END, "you : " + query)
    print(type(answer_from_Sam))
    msgs.insert(END, "Sam : " + str(answer_from_Sam))
    textF.delete(0,END)

Frame=Frame(main)
sc=Scrollbar(Frame)
msgs=Listbox(Frame,width=80,height=10,yscrollcommand=sc.set)
sc.pack(side=RIGHT,fill=Y)
msgs.pack(side=LEFT,fill=BOTH,pady=10)
Frame.pack()

textF = Entry(main, font=('Vardana',20))
textF.pack(fill=X,pady=10)

btn = Button(main, text='Ask from Sam', font=('Verdana',20),command=Ask_from_Sam)
btn.pack()

def enter_function(Event):
    btn.invoke()


main.bind('<Return>',enter_function)

def repeatL():
    while True:
        takeQuery()

t=threading.Thread(target=repeatL)

t.start()

main.mainloop()