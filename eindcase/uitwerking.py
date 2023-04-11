from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/readfile')
def read_file():
    filename = request.args.get('filename')
    try:
        with open(filename, 'r') as file:
            data = file.read()
            return data
    except Exception as e:
        return str(e)

@app.route('/writefile', methods=['POST'])
def write_file():
    filename = request.args.get('filename')
    data = request.form.get('data')
    try:
        with open(filename, 'w') as file:
            file.write(data)
            return 'File written successfully'
    except Exception as e:
        return str(e)

@app.route('/deletefile', methods=['DELETE'])
def delete_file():
    filename = request.args.get('filename')
    try:
        os.remove(filename)
        return 'File deleted successfully'
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run()
