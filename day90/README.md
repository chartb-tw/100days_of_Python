# The text-to-speech API

This is the day 90 project, broken down into two parts:
1. A Jupyter Notebook that I had used to do some investigating into different .pdf readers and TTS services
2. A script that takes the .pdf file and converts it into an .mp3 file

There is a way to do it without using an API (notably the gtts module), however I had wanted to make sure I used an API in line with the project specifications.
I ended up using Google's API in the end, along with some documentation reading to figure out how to create the .mp3 file from the response given. The .pdf was parsed using the fitz module.
Of course, by reading the notebook (and my inane ramblings to myself, as per these READMEs) you'll realise that things can change and a package that worked in the past may not be suitable these days!

(s, rrx)
