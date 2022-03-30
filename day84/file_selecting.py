import datetime as dt

import tkinter as tki
from tkinter import filedialog, messagebox

# the filetypes parameter of
image_file_types = [
			("Image types", ("*.png", "*.PNG", "*.jpg", "*.JPG", "*.jpeg", "*.JPEG", "*.gif", "*.GIF")),
			("All file types", "*.*"),
			]

window = tki.Tk()

window.title("File processor")
window.config(padx=50, pady=50)


def UploadAction(event=None):
	ask_filename = filedialog.askopenfilename(filetypes=image_file_types) # the filetypes parameter of askopenfilename is optional, but allows for only specific file types to be selected or to filter by separate types
	if len(ask_filename)!=0:
		global filename
		filename = ask_filename
		file_label.config(text = f"File chosen: {filename}")
	
def clear_chosen_file(event=None):
	if "filename" in globals(): # globals() is a list of the global variables named
		global filename
		del filename
	file_label.config(text = "Select file:")

def file_processing_func():
	try:
		if "filename" in globals():
			global filename
		"""
		# this else is unnecessary, as the filename won't be defined when called below!
		else:
			raise NameError("No file has been selected") # raise (throw) a NameError if no file was defined
		"""
		file = open(filename, "r") # a NameError will occur if no file was defined
		print(f"File \"{filename}\" opened")
		print(f"Text entered in box: \"{watermark_entry.get()}\"")
	except FileNotFoundError: # a file could be deleted/moved after it was selected
		messagebox.showerror(title= "Error opening input file",message=f"The file:\n{filename}\" could not be found. Was the file deleted or moved after selection?")
	except NameError: # catch the NameError if the filename wasn't defined
		messagebox.showwarning(title="No file selected", message="No file was selected")
	except UnicodeDecodeError:
		messagebox.showerror(title= "Error opening input file", message=f"The file:\n{filename}\" could not be opened. The filename has Unicode characters that could not be processed.")
	else:
		print("No errors happened")
	finally:
		if ("file" in locals()): # locals() is a list of the local variable names
			file.close() # close the file if the file was defined (e.g. if the file was opened)
			messagebox.showinfo(title="Success", message=f"File \"{filename}\" opened and closed successfully")
			clear_chosen_file()
		
watermark_label = tki.Label(text = "Choose text:")
watermark_label.pack()

watermark_entry = tki.Entry(width = 35)
watermark_entry.pack()

file_label = tki.Label(text = "Select file:")
file_label.pack()

upload_button = tki.Button(window, text='Select file', command=UploadAction)
upload_button.pack()

clear_button = tki.Button(window, text='Clear file', command=clear_chosen_file, bg="#FF0000", activebackground="#FF5700")
clear_button.pack()

process_button = tki.Button(window, text='Process', command=file_processing_func)
process_button.pack()

window.mainloop()
