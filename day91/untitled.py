#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  untitled.py
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



from flask import Flask, render_template, redirect, url_for
import datetime as dt
import numpy as np
from PIL import Image # for reading image files

from flask_wtf import FlaskForm
import wtforms.fields as wtfields
from flask_bootstrap import Bootstrap

from flask_wtf.file import FileField, FileAllowed, FileRequired
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

allowed_image_typelist = ["png", "PNG", "jpg", "JPG", "jpeg", "JPEG", "gif", "GIF"]


class FileForm(FlaskForm):
	file_name = FileField(validators=[FileRequired(), FileAllowed(allowed_image_typelist, 'PNG/JPG/GIF images only!')])
	submit = wtfields.SubmitField('Submit')

def rgb_to_hex(rgb):
    r,g,b = rgb[:3]
    return '#%02x%02x%02x' % (r,g,b)

# homepage

@app.route('/', methods = ["GET","POST"])
def home():
	photo_ff = FileForm()
	if photo_ff.validate_on_submit():
		image_fp = photo_ff.file_name.data
		filename = secure_filename(image_fp.filename)
		savepath = f'static/uploads/{filename}'
		image_fp.save(savepath)
		
		img_open = Image.open(savepath)
		img = np.array(img_open)
		img_array = img.copy()
		img_array.shape = ((img_array.shape[0] * img_array.shape[1]),img_array.shape[2],)


		based = np.unique(img_array, return_counts=True, axis=0)
		value_and_count = list(zip(based[0], based[1]))
		value_and_count.sort(key = lambda x : x[1])
		
		most_pop_colors = value_and_count[-10:][::-1]
		
		print('\n', f"filepath: {savepath}", '\n\n', most_pop_colors, '\n')
		
		colList = [(rgb_to_hex(x[0]), x[1]) for x in most_pop_colors]
		fileLoc = filename
		
		return render_template("homepage.html", col_list = colList, embedImg = fileLoc, tot_pixels = len(value_and_count), form = photo_ff, rn = dt.datetime.now())
	return render_template("homepage.html", form = photo_ff, rn = dt.datetime.now())
	



if __name__ == "__main__":
	app.run(debug=True)
