from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'message': 'Wow, this is an app!'})


if __name__ == '__main__':
    app.run()