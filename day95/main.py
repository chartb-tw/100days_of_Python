from flask import Flask, render_template
import datetime as dt
import requests
# import bs4

endp = "https://api.rtt.io/api/v1/"
api_cred = ("USERNAME", "PASSWORD") # get these from api.rtt.io

app = Flask(__name__)


@app.route('/')
def home(): 
	return render_template("homepage.html", rn = dt.datetime.now())

@app.route('/<string:train_loc>')
def station_dep(train_loc): 
	resp = requests.get(url = f"{endp}json/search/{train_loc}", auth = api_cred)
	resp.raise_for_status()
	dep_services = resp.json()
	return render_template("stations.html", rn = dt.datetime.now(), services = dep_services["services"], station_name = dep_services["location"]["name"])




if __name__ == "__main__":
	app.run(debug=True)
