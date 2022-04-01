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

# location line up - docs at https://www.realtimetrains.co.uk/about/developer/pull/docs/locationlist/
@app.route('/<string:train_loc>')
def station_dep(train_loc): 
	resp = requests.get(url = f"{endp}json/search/{train_loc}", auth = api_cred)
	resp.raise_for_status()
	dep_services = resp.json()
	return render_template("stations.html", rn = dt.datetime.now(), services = dep_services["services"], station_name = dep_services["location"]["name"])

# service info - docs at https://www.realtimetrains.co.uk/about/developer/pull/docs/serviceinfo/
@app.route('/train/<serviceUid>/<year>/<month>/<day>')
def train_detail(serviceUid, year, month, day):
	resp = requests.get(f"{endp}json/service/{serviceUid}/{year}/{month}/{day}", auth = api_cred)
	# resp.raise_for_status()
	return jsonify(resp.json()) # Could have built this into a page, may do so at another date

@app.route('/train/<serviceUid>')
def train_detail_now(serviceUid):
	rnow = dt.datetime.now()
	return redirect(url_for('train_detail', serviceUid = serviceUid, year = rnow.strftime('%Y'), month = rnow.strftime('%m'), day = rnow.strftime('%d')))

@app.route('/train')
def cba_to_implement():
	return redirect(url_for('home'))


if __name__ == "__main__":
	app.run(debug=True)
