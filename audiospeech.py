import speech_recognition as sr
r = sr.Recognizer()

file_audio = sr.AudioFile('Sample.wav')


with file_audio as source:
   audio_text = r.record(source)

print('Reading sound format and converting...')
#print(r.recognize_google(audio_text))

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 0

    return counts
#print( word_count(r.recognize_google(audio_text)))
