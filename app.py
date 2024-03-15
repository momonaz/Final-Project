from flask import Flask, render_template, request
from functions import get_plant_info

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        plant_name = request.form.get("plant_name")
        api_key = "a934db7ornxS2TrWNztoLRdafZo6ZDEv3Sip1GaUZL0"
        plant_info = get_plant_info(plant_name, api_key)
        return render_template('index.html', plant_info=plant_info)
    else:
        return render_template('index.html', plant_info=None)

if __name__ == "__main__":
    app.run(debug=True)