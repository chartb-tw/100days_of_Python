from flask import Flask, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, NumberRange
import wtforms.fields as wtfields
from flask_sqlalchemy import SQLAlchemy
#import csv
import datetime as dt

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

API_KEY = "lolYouNeek"

class CafeForm(FlaskForm):
	cafe_name = wtfields.StringField('Cafe name', validators=[DataRequired()])
	cafe_url = wtfields.URLField("Cafe location on maps (URL)", validators=[DataRequired()])
	img_url = wtfields.URLField("Image link (URL)", validators=[DataRequired()])
	location = wtfields.StringField('Location', validators=[DataRequired()])
	#seats = wtfields.IntegerField("Seats", validators=[DataRequired(), NumberRange(min=0)])
	seats = wtfields.SelectField('Number of seats', choices=['0-10', '10-20', '20-30', '30-40', '40-50', '50+']) # SelectFields cam take (value,label) pairs, or values which will also be used as labels
	has_toilet = wtfields.BooleanField("Toilet available?")
	has_wifi = wtfields.BooleanField("WiFi available?") 
	has_sockets = wtfields.BooleanField("Power sockets avaiable?")
	can_take_calls = wtfields.BooleanField("Can take calls?")
	coffee_price = wtfields.DecimalField('Coffee price', validators=[NumberRange(min=0)]) # ... we could be cheeky and allow negative prices - make them pay you to drink coffee! But here I'm being good
	submit = wtfields.SubmitField('Submit')

class DeleteForm(FlaskForm):
	api_key = wtfields.PasswordField("Delete key", validators=[DataRequired()])
	submit = wtfields.SubmitField('Delete cafe')

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)
    
    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


# all Flask routes below

@app.errorhandler(404)
def not_found_page(e):
	return render_template("error_404.html", rn = dt.datetime.now()), 404

@app.route("/")
def home():
	return render_template("index.html", rn = dt.datetime.now())


@app.route('/add', methods = ["GET","POST"])
def add_cafe():
	form = CafeForm()
	if form.validate_on_submit():
		# print(form.data)
		form_data = form.data.copy()
		cafe_check = Cafe.query.filter_by(name = form_data["cafe_name"]).first() # the cafe name must be unique, so check if the name already appears
		if cafe_check: # if a cafe with the name alrady exists, say so and take them to the cafes
			flash(f"A cafe with the same name ({form_data['cafe_name']}) already exists. Check whether the cafe already is in the list, or otherwise modify the name with the location or a number?")
			return redirect(url_for('cafes'))
		else: # if not, then (should be able to) add it with no worries
			new_cafe = Cafe(name = form_data["cafe_name"], map_url = form_data["cafe_url"], img_url = form_data["img_url"], location = form_data["location"],
				seats = form_data["seats"], has_toilet = form_data["has_toilet"], has_wifi = form_data["has_wifi"], has_sockets = form_data["has_sockets"],
				can_take_calls = form_data["can_take_calls"], coffee_price = format(float(form_data["coffee_price"]), ".2f"))
			db.session.add(new_cafe)
			db.session.commit()
			flash(f"Your cafe \"{form_data['cafe_name']}\" has been added!")
			return redirect(url_for('cafes'))		
	return render_template('add.html', form=form, cafeid = None, rn = dt.datetime.now())



@app.route('/cafes')
def cafes():
	all_the_cafes = db.session.query(Cafe).all()
	return render_template('cafes.html', all_cafes = all_the_cafes, rn = dt.datetime.now())

@app.route('/cafes/<int:cafe_id>')
def given_cafe(cafe_id):
	cafe_to_show = Cafe.query.get(cafe_id)
	if cafe_to_show:	
		return render_template('specific_cafe.html', cafe_to_show = cafe_to_show, rn = dt.datetime.now())
	else: # otherwise say that it isn't there
		flash("The requested cafe could not be found. It probably was deleted already?")
		return redirect(url_for('cafes'))
		

@app.route('/edit/<int:cafe_id>', methods = ["GET","POST"])
def edit_cafe(cafe_id):
	cafe_to_edit = Cafe.query.get(cafe_id)
	if cafe_to_edit: # if you find the cafe, edit it
		edit_form = CafeForm(cafe_name = cafe_to_edit.name, cafe_url = cafe_to_edit.map_url, img_url = cafe_to_edit.img_url, location = cafe_to_edit.location, 
								seats = cafe_to_edit.seats, has_toilet = cafe_to_edit.has_toilet, has_wifi = cafe_to_edit.has_wifi, has_sockets = cafe_to_edit.has_sockets,
								can_take_calls = cafe_to_edit.can_take_calls, coffee_price = float(cafe_to_edit.coffee_price))
		if edit_form.validate_on_submit():
			form_data = edit_form.data
			cafe_to_edit.name = form_data["cafe_name"] 
			cafe_to_edit.map_url = form_data["cafe_url"] 
			cafe_to_edit.img_url = form_data["img_url"] 
			cafe_to_edit.location = form_data["location"]
			cafe_to_edit.seats = form_data["seats"]
			cafe_to_edit.has_toilet = form_data["has_toilet"]
			cafe_to_edit.has_wifi = form_data["has_wifi"]
			cafe_to_edit.has_sockets = form_data["has_sockets"]
			cafe_to_edit.can_take_calls = form_data["can_take_calls"]
			cafe_to_edit.coffee_price = format(float(form_data["coffee_price"]), ".2f")
			db.session.commit()
			flash(f"Your cafe edit to \"{cafe_to_edit.name}\" has successfully been made.")
			return redirect(url_for('cafes'))
		return render_template('add.html', form=edit_form, cafeid = cafe_id, rn = dt.datetime.now())
	else: # otherwise say that it isn't there
		flash("The requested cafe could not be found. It probably was deleted?")
		return redirect(url_for('cafes'))

@app.route('/delete/<int:cafe_id>', methods = ["GET","POST"])
def delete_cafe(cafe_id):
	cafe_to_delete = Cafe.query.get(cafe_id)
	if cafe_to_delete: # if you can find the cafe, prepare to delete it
		cafe_del_name = cafe_to_delete.name
		del_form = DeleteForm()
		if del_form.validate_on_submit():
			if del_form.data["api_key"]==API_KEY:
				db.session.delete(cafe_to_delete)
				db.session.commit()
				flash(f"The cafe \"{cafe_del_name}\" was successfully deleted.")
				return redirect(url_for('cafes'))
			else:
				flash("The key you provided was not correct. Please try again.")
				return redirect(url_for('delete_cafe', cafe_id=cafe_id))
		return render_template("delete.html", cafe= cafe_to_delete, form = del_form, rn = dt.datetime.now())
	else: # otherwise say that it isn't there
		flash("The requested cafe could not be found. It probably was deleted already?")
		return redirect(url_for('cafes'))

if __name__ == '__main__':
	app.run(debug=True)

