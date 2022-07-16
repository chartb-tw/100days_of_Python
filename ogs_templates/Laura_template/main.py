#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  untitled.py
#  
#  Copyright 2022 charles <charles@MacBook-Air>
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

from flask import Flask, render_template, redirect, url_for, jsonify
import datetime as dt
import requests

app = Flask(__name__)


@app.errorhandler(404)
def not_found_page(e):
	return render_template("404-page.html", rn = dt.datetime.now(), transparent_header = False), 404

@app.route('/')
def home(): 
	return render_template("index.html", rn = dt.datetime.now(), transparent_header = True)

@app.route('/details')	
def portfolio_details():
	return render_template("portfolio-details.html", rn = dt.datetime.now(), transparent_header = False)
	
@app.route('/inner-page')
def inner_page():
	return render_template("inner-page.html", rn = dt.datetime.now(), transparent_header = False)

if __name__ == "__main__":
	app.run(debug=True)
