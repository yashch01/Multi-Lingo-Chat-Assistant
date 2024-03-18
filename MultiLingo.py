import openai #library for linking witrh chatgpt
from googletrans import Translator #library for linking with google translator
import pyttsx3 #text to speech
import speech_recognition as sr #library for taking voice input
def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return data

translator = Translator()   #object of translator class 
s=recordAudio() 
openai.api_key="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"
eng=pyttsx3.init() #engine setup for text to speech
rate=eng.getProperty('rate')
voices=eng.getProperty("voices")
eng.setProperty('rate',125)
eng.setProperty('voice',voices[0].id)
eng.say(s) #speaking of question
eng.runAndWait() #text to speech and provide some gap

eng.say("Please wait while we finding your answer")
eng.runAndWait()
detected=translator.detect(s)
d=(translator.translate(s,src=detected.lang,dest='english').text)
completion= openai.Completion.create(
                model="text-davinci-003",
                prompt=d,
                max_tokens=1000
            )

print(completion.choices[0]["text"])
response=completion.choices[0]["text"]
print(translator.translate(response,src='english',dest=detected.lang).text)