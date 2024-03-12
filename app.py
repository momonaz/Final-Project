from flask import Flask, render_template
from functions import get_plant_info

app = Flask(__name__)

@app.route("/")
def index():
    # Your plant name
    plant_name = "Rosa arvensis"
    # Your Trefle API key
    api_key = "a934db7ornxS2TrWNztoLRdafZo6ZDEv3Sip1GaUZL0"
    plant_info = get_plant_info(plant_name, api_key)
    return render_template('index.html', plant_info=plant_info)

if __name__ == "__main__":
    app.run(debug=True)
