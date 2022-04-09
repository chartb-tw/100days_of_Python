#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  morse_code_cmdlprog.py
#  
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import json
"""
# Run the below to get the .json used, or comment this out to use the provided one
import bs4
import requests

resp = requests.get("https://sckans.edu/~sireland/radio/code.html")
resp.raise_for_status()
soup = bs4.BeautifulSoup(resp.text,"html.parser")

pa_list = soup.find_all(name="table")[0].find_all(name = "tr")[1:]
pa_dict = {}
for alph in pa_list:
	pa_dict[alph.find_all(name = "td")[0].getText().strip()]=alph.find_all(name = "td")[1].getText().strip()
pa_numlist = soup.find_all(name="table")[1].find_all(name = "tr")[1:]
for num in pa_numlist:
	pa_dict[num.find_all(name = "td")[0].getText().strip()] = num.find_all(name = "td")[1].getText().strip()

# run the below to save a .json file
with open("morse_code.json",'w') as file:
    json.dump(pa_dict, file)
    
# run the below to use the same dictionary fetched
morse_dict = pa_dict
"""
# run the below to use the genrated .json file
with open("morse_code.json",'r') as file:
	morse_dict = json.load(file)

while True:	
	usr_req = input("Give a word, and we'll convert the alphanumeric characters into Morse Code: ").upper()
	out = []
	for char in usr_req:
		if char in morse_dict.keys():
			out.append(morse_dict[char])
	print(out)
	keep_going = input("Would you like another? ([y]/n): ").lower()
	if (keep_going=="n") or (keep_going=="no"):
		print("Goodbye, thank you for using our program! 🥰")
		break
	elif (keep_going!="y") and (keep_going!="yes") and (keep_going!=""):
		print("Sorry, I couldn't get that input.\nIf you'd Like to terminate, give any input in the next step and type 'n' or 'no' in this promt.\n")
	else:
		print("Okay cool, we'll run the program again!\n")
