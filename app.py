from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

# Function to fetch price data from the API
def fetch_price(hour=0):
    url = f"https://api.spot-hinta.fi/JustNow?lookForwardHours={hour}"
    response = requests.get(url)
    data = response.json()
    # Extracting PriceWithTax and DateTime
    price_with_tax = data['PriceWithTax']
    time = data['DateTime']
    return {'price': price_with_tax, 'time': time}

# Endpoint to get the current price and next hour price
@app.route('/get_prices')
def get_prices():
    current_price = fetch_price(0)  # Fetch current hour price
    next_hour_price = fetch_price(1)  # Fetch next hour price
    return jsonify({'current': current_price, 'next': next_hour_price})

# Render the web page
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)