from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/static/app.js')
def serve_static_app():
    return send_from_directory('static', "app.js")

@app.route('/map/app.js.map')
def serve_static_map():
    return send_from_directory('map', "app.js.map")

@app.route('/')
def serve_index():
    return send_from_directory('static', 'index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
