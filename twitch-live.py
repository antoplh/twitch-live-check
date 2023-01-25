from flask import Flask, jsonify, make_response
import requests

app = Flask(__name__)

@app.route('/')
def index():
    html = """
    <html>
        <body>
            <h1>Welcome to the Livestreamer API</h1>
            <form action="{{ url_for('is_live', channel_name=channel_name) }}" method="get">
                <label>Enter the channel name you want to check:</label>
                <input type="text" name="channel_name">
                <input type="submit" value="Submit">
            </form>
        </body>
    </html>
    """
    return make_response(html)

@app.route('/<channel_name>', methods=['GET'])
def is_live(channel_name):
    response = requests.get(f"https://www.twitch.tv/{channel_name}")
    if "isLiveBroadcast" in response.text:
        res = make_response(jsonify({"status": "live"}))
    else:
        res = make_response(jsonify({"status": "offline"}))
    res.headers.add("Access-Control-Allow-Origin","*")
    return res
    
if __name__ == '__main__':
    app.run( debug=True)
