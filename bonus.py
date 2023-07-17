import speech_recognition as sr

#obtain audio from the microphone
def getAudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("say somthing: ")
        audio = r.listen(source)

    # recognize speech using Sphinx
    try:
        print("the text you said:", r.recognize_sphinx(audio))
        return r.recognize_sphinx(audio)
    except sr.UnknownValueError:
        print("didnt uunderstand what you said be more clear!!!")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))