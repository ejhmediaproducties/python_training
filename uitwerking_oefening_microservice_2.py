from flask import Flask

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello_world():
    return 'Hello, World!'

@app.route('/goodbye', methods=['GET'])
def goodbye_world():
    return 'Goodbye, World!'

@app.route('/name/<name>', methods=['GET'])
def hello_name(name):
    return f'Hello, {name}!'

if __name__ == '__main__':
    app.run()
