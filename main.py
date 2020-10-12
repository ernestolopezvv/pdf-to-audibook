# Program to transform pdf to audiobook

import pyttsx3
import PyPDF2

book = open('Audiobook.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
page = pdfReader.getPage(0)
text = page.extractText()
speaker.say(text)
speaker.runAndWait()

# If you want the spanish voice import this at first and then paste this in line 15
# es_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0"
# speaker.setProperty('voice', es_voice_id)
# speaker.setProperty('voice', es_voice_id)


