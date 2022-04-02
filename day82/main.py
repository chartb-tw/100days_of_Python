from flask import Flask, render_template
import datetime as dt


app = Flask(__name__)

# 404 page
@app.errorhandler(404)
def not_found_page(e):
	return render_template("error_404.html", rn = dt.datetime.now()), 404



# homepage

@app.route('/')
def home(): 
	return render_template("homepage.html", rn = dt.datetime.now())



# productions base page
	
@app.route('/productions')
def productions_page(): 
	return render_template("productions.html", rn = dt.datetime.now())



# Help and info page
	
@app.route('/help')
def help_page(): 
	return render_template("helpme.html", rn = dt.datetime.now())



# About and contact page
	
@app.route('/about-contact')
def about_page(): 
	return render_template("about_contact.html", rn = dt.datetime.now())



# privacy page
	
@app.route('/privacy')
def privacy_page(): 
	return render_template("privacy.html", rn = dt.datetime.now())


"""
# test page - not implemented here
	
@app.route('/testing')
def testing_page(): 
	return render_template("testing.html", rn = dt.datetime.now())
"""


if __name__ == "__main__":
	app.run(debug=True)
