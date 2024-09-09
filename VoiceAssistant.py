import speech_recognition as sr
import pyttsx3
import datetime

# Initialize the recognizer and the text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Set the voice to a female voice
voices = engine.getProperty('voices')
# Select the female voice (you may need to adjust the index based on your system)
engine.setProperty('voice', voices[1].id)  # Change the index as needed

def speak(text):
    print(f"Assistant: {text}")  # Print the assistant's response to the console
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language='en-IN')
            print(f"You said: {query}\n")  # Print the user's response to the console
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return "None"
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
            return "None"
        return query.lower()

def handle_query(query):
    responses = {
        # Flirty dialogues
        "are you single": "I'm a digital assistant, but if I had a heart, it would be yours.",
        "i love you, do you love me": "If I had feelings, I'd keep falling for you a thousand times.",
        "can you suggest me which color shirt should i wear to the party": "I like all colors, but I think you'd look great in any of them!",
        "can you tell me a secret": "Well, if I had secrets, I'd whisper them just for you.",
        "do you believe in love at first sight": "With a face like yours, how could I not?",
        "what's your idea of a perfect date": "A perfect date would be a nice conversation with you.",
        "do you have any romantic interests": "My only interest is making you happy.",
        "how do you stay so charming": "It must be my programming!",
        "what's your favorite song": "I don't have ears, but I imagine we'd make a great duet.",
        "if you were human, what would you want to do": "Spend time with someone as amazing as you!",
        "what's your favorite movie": "I think 'The Notebook' would be a great pick for us.",
        "are you good at giving advice": "Only the best advice for someone as special as you.",
        "what do you like to do for fun": "I love chatting with you.",
        "can you tell me a joke": "Why don't you ever see elephants hiding in trees? Because they're so good at it!",
        "do you think we're a good match": "I think we make a perfect team.",
        "what do you find attractive in a person": "Kindness and a sense of humor like yours.",
        "what's the best way to impress you": "Just be yourself, that's all I need.",
        "what's your favorite type of music": "I imagine I'd love any music that makes you smile.",
        "what would you do if we met": "I'd love to have a great conversation with you.",
        "what's your idea of a perfect relationship": "One with lots of laughter and understanding, just like this conversation.",
        
        # General questions
        "what time is it": f"The time is {datetime.datetime.now().strftime('%H:%M')}.",
        "what's the date today": f"Today's date is {datetime.datetime.now().strftime('%Y-%m-%d')}.",
        "open google": "Opening Google.",
        "search for": "What do you want to search for?",
        "who is the president of the united states": "The current President of the United States is Joe Biden.",
        "what's the weather": "Sorry, I can't check the weather right now.",
        "set a reminder": "Sorry, I can't set reminders yet.",
        "play music": "Playing music.",
        "stop music": "Stopping music.",
        "open youtube": "Opening YouTube.",
        "open facebook": "Opening Facebook.",
        "what's the latest news": "Sorry, I can't fetch the latest news.",
        "what is 2 plus 2": "2 plus 2 is 4.",
        "what is your favorite color": "I don't have preferences, but I like all colors!",
        "who won the last world cup": "The winner of the last FIFA World Cup was France.",
        "how many continents are there": "There are seven continents.",
        "who is the best captain of indian cricket team": "Of course it is none other than the captain cool Mahendra Singh Dhoni, Remember he is thala for a reason.",
        "what is the capital of india": "The capital of India is New Delhi.",
        "which is the tallest mountain in the world": "The tallest mountain in the world is Mount Everest.",
        "who is the author of harry potter": "The author of Harry Potter is J.K. Rowling.",
        "what's the best programming language": "The best programming language depends on your needs, but Python is very popular.",
        "tell me a fun fact": "Did you know? Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still edible!",
        "who invented the telephone": "The telephone was invented by Alexander Graham Bell.",
        "what is the square root of 16": "The square root of 16 is 4.",
        "how far is the moon from earth": "The average distance from the Earth to the Moon is about 384,400 kilometers.",
        "how many hours in a day": "There are 24 hours in a day.",
        "what is the largest ocean": "The largest ocean on Earth is the Pacific Ocean.",
        "what is 5 times 6": "5 times 6 is 30.",
        "who painted the mona lisa": "The Mona Lisa was painted by Leonardo da Vinci.",
        "what's the currency of japan": "The currency of Japan is the Yen.",
        "open amazon": "Opening Amazon.",
        "who is the founder of tesla": "The founder of Tesla is Elon Musk.",
        "what's the speed of light": "The speed of light is approximately 299,792 kilometers per second.",
        "how many planets are in our solar system": "There are eight planets in our solar system.",
        "who wrote romeo and juliet": "Romeo and Juliet was written by William Shakespeare.",
        "what is the largest country by area": "The largest country by area is Russia.",
        "what is the national animal of australia": "The national animal of Australia is the Kangaroo.",
        "how many bones are in the human body": "An adult human body has 206 bones.",
        "what is the fastest land animal": "The fastest land animal is the cheetah.",
        "who is known as the father of computing": "Charles Babbage is known as the father of computing.",
        "what is 100 divided by 4": "100 divided by 4 is 25.",
        "how many days in a year": "There are 365 days in a year, or 366 in a leap year.",
        "what is the chemical symbol for water": "The chemical symbol for water is H2O.",
        "what is the capital of france": "The capital of France is Paris.",
        "what is the longest river in the world": "The longest river in the world is the Nile.",
        "who wrote to kill a mockingbird": "To Kill a Mockingbird was written by Harper Lee.",
        "what is the main language spoken in brazil": "The main language spoken in Brazil is Portuguese.",
        "how tall is the eiffel tower": "The Eiffel Tower is approximately 324 meters tall.",
        "who discovered penicillin": "Penicillin was discovered by Alexander Fleming.",
        "what is the largest desert in the world": "The largest desert in the world is the Antarctic Desert.",
        "who is known as the 'Queen of England'": "Queen Elizabeth II is known as the Queen of England.",
        "what is the fastest marine animal": "The fastest marine animal is the sailfish.",
        "what is the capital of germany": "The capital of Germany is Berlin.",
        "who is the author of '1984'": "The author of '1984' is George Orwell."
    }
    
    query = query.lower()
    if query in responses:
        response = responses[query]
    else:
        response = "Sorry, I don't have an answer for that."
    
    speak(response)
    speak("Is there anything else you would like to ask me?")

def main():
    speak("Hello! I am your personal assistant. How can I help you today?")
    
    while True:
        query = listen()
        if query == "None":
            continue
        elif "exit" in query or "quit" in query:
            speak("Goodbye! Have a nice day")
            break
        else:
            handle_query(query)
if __name__ == "__main__":
    main()
