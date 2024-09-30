from flask import Flask, jsonify, send_file
import requests

app = Flask(__name__)

@app.route('/')
def serve_html():
    return send_file('energy_prices.html')

@app.route('/JustNow')
def fetch_energy_prices():
    look_forward_hours = request.args.get('lookForwardHours', 0)
    is_html_request = request.args.get('isHtmlRequest', 'true')

    api_url = f"https://api.spot-hinta.fi/JustNow?lookForwardHours={look_forward_hours}&isHtmlRequest={is_html_request}"
    response = requests.get(api_url)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)