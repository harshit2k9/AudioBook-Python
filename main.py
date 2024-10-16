import pdfplumber
from gtts import gTTS
pdfPath = "file.pdf"
print("Please make sure the file uploaded is named as "file.pdf)
pdf =  pdfplumber.open(pdfPath)
text = ''
for i in range(1,5):
  page = pdf.pages[i]
  text = text +  page.extract_text()
pdf.close
language ='en'
gtts_transformer=gTTS(text=text, lang = language)
gtts_transformer.save("My Audio.mp3")
print("Converted")
