from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello CI/CD! This is a simple  application."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)