from transformers import pipeline
import pyttsx3
import speech_recognition as sr

# Emotion analysis pipeline
emotion_recognizer = pipeline("sentiment-analysis")

# For TTS Engine, you can remove this if u want
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... Please talk...")
        audio = recognizer.listen(source)
        try:
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return "Sorry, I didn't understand that, please try again!"
        except sr.RequestError:
            return "Sorry, Something went wrong with the speech service."

def generate_response(text):
    emotion = emotion_recognizer(text)
    emotion_label = emotion[0]['label']
    
    if emotion_label == 'POSITIVE':
        return "It seems you feeling good!"
    elif emotion_label == 'NEGATIVE':
        return "It seems you feeling bad!"
    else:
        return "Yeah, I see!"

if __name__ == "__main__":
    print("How are you feeling today, please talk!")
    speak("How are you feeling today, please talk!")
    
    user_input = listen()
    print(f"You said: {user_input}")
    
    response = generate_response(user_input)
    print(f"PyVoiceMood: {response}")
    speak(response)
