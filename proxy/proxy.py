import flask
from flask import request, jsonify
import requests

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Define the base URL of the Express API
EXPRESS_API_URL = "http://localhost:3000"
def proxy_request(endpoint, method, data=None, headers=None):
    express_api_url = f"{EXPRESS_API_URL}/{endpoint}"
    try:
        response = requests.request(method, express_api_url, data=data, headers=headers)
        return (response.content, response.status_code, response.headers.items())
    except Exception as e:
        print(f"Error making request to Express API: {e}")
        return ("Internal Server Error", 500, [])

# Generic route handler
@app.route('/api/<path:endpoint>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def handle_proxy(endpoint):
    return proxy_request(endpoint, request.method, request.data, dict(request.headers))



# Run the Flask app on port 5001
if __name__ == '__main__':
    app.run(port=5001)
