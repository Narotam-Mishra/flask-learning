from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'flask' and password == 'password':
            return 'Success'
        else:
            return 'Failure'

@app.route('/file_upload', methods=['POST'])
def file_upload():
    file = request.files['file']

    if file.content_type == 'text/plain':
        return file.read().decode()
    
@app.route('/handle_post', methods=['post'])
def handle_post():
    greeting = request.json['greeting']
    name = request.json['name']

    with open('file.txt', 'w') as f:
        f.write(f'{greeting}, {name}')

    return jsonify({'message': 'Successfully written!'})   

if __name__ == '__main__':
    app.run(port=5576, debug=True)