from flask import Flask, render_template, request, after_this_request, jsonify

app = Flask(__name__, static_folder='static', static_url_path='')


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/citation', methods=['GET'])
def citation_challenge():
    return render_template('citation.html')


@app.route('/nettoyage', methods=['GET'])
def nettoyage_challenge():
    return render_template('nettoyage.html')


@app.route('/peinture', methods=['GET'])
def peinture_challenge():
    return render_template('peinture.html')


@app.route('/tresors/1', methods=['GET', 'POST'])
def tresor1_challenge():
    if request.method == 'GET':
        return render_template('tresor1.html')

    if request.method == 'POST':
        key = request.get_json().get('key')

        @after_this_request
        def add_header(response):
            response.headers['Access-Control-Allow-Origin'] = '*'
            return response
        if key == "captain":
            flag = {'flag': "flag-C4PT41N-H3R3"}
        else:
            flag = {'flag': ":("}

        return jsonify(flag)


@app.route('/tresors/2', methods=['GET', 'POST'])
def tresor2_challenge():
    if request.method == 'GET':
        return render_template('tresor2.html')

    if request.method == 'POST':
        key = request.get_json().get('key')
        twoFA = request.get_json().get('twoFA')

        @after_this_request
        def add_header(response):
            response.headers['Access-Control-Allow-Origin'] = '*'
            return response
        if key == "captain" and twoFA == "85427936":
            flag = {'flag': "flag-S3CR3T-F0UND"}
        else:
            flag = {'flag': ":("}

        return jsonify(flag)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
