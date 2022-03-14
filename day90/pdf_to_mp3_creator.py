import fitz
import requests
import os

saved_api_key = "AIzaSyB5Hty3AjEq-NLGGqTpEFelA2--VgMO7_g"

fname_given = input("Type the filename of the .pdf that you would like to convert: ")
if fname_given[-4:]!=".pdf":
	fname_given = f"{fname_given}.pdf"
print("Opening and processing the file. This may take some time...")
doc_mr = fitz.open(fname_given)
output_string = ""
for page in doc_mr:
    output_string += (" " + page.get_text()) 

print("Done.\nConverting the text into a .mp3 via an API, this might also take some time (and requires an internet connection...)")

gctts_url = f"https://texttospeech.googleapis.com/v1/text:synthesize?key={saved_api_key}"
gctts_paramets = {
  "audioConfig": {
    "audioEncoding": "MP3"
  },
  "voice": {
    "languageCode": "en"
  },
  "input": {
    "text": output_string[:5000]
  }
} # there is a 5000 character limit to the api
#gctts_headers = {"key" : saved_api_key}
resp = requests.post(url = gctts_url, json = gctts_paramets) #, headers = gctts_headers)
resp.raise_for_status()

print("Done. Now saving your file...")

file_ttf = open("synthesize-text.txt","w")
file_ttf.write(resp.json()["audioContent"])
file_ttf.close()

os.system(f"base64 synthesize-text.txt --decode > {fname_given[:-4]}.mp3")
os.system("rm synthesize-text.txt")
print(f"Your audiobook is saved as {fname_given[:-4]}.mp3. Enjoy!")
