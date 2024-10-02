from flask import Flask, jsonify, render_template
import requests
import json
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__, static_folder='../')

def get_spot_prices():
    # Define URLs for current and next hour prices
    current_url = "https://api.spot-hinta.fi/JustNow?lookForwardHours=0"
    next_hour_url = "https://api.spot-hinta.fi/JustNow?lookForwardHours=1"

    # Make separate requests for each URL
    current_response = requests.get(current_url)
    next_hour_response = requests.get(next_hour_url)

    # Check for successful responses
    if current_response.ok and next_hour_response.ok:
        # Parse JSON responses
        current_data = current_response.json()
        next_hour_data = next_hour_response.json()

        # Format data for easier handling in HTML
        data = {
            "current": {
                "price": current_data["PriceWithTax"],
                "time": current_data["DateTime"]
            },
            "next_hour": {
                "price": next_hour_data["PriceWithTax"],
                "price_no_tax": next_hour_data["PriceNoTax"],  # Include additional data if needed
                "time": next_hour_data["DateTime"]
            }
        }

        return data
    else:
        # Handle errors gracefully
        print("Error fetching data:", current_response.status_code, next_hour_response.status_code)
        return None

def update_data_file():
    prices = get_spot_prices()
    if prices:
        with open("data.json", "w") as f:
            json.dump(prices, f)

# Background scheduler setup (adjust interval as needed)
scheduler = BackgroundScheduler()
scheduler.add_job(update_data_file, 'interval', seconds=10)  # Update every 10 seconds
scheduler.start()

@app.route("/")
def index():
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = None  # Handle missing file gracefully

    return render_template("index.html")

@app.route("/data.json")
def get_data_file():
  return send_file("data.json")

if __name__ == "__main__":
    app.run(debug=True)