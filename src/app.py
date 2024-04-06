from flask import Flask, jsonify

app = Flask(__name__)

@app.errorhandler(Exception)
def handle_exception(e):
    # you can exclude the exception name (e.g., "Exception: ") from the str representation
    response = {
        "error": "A server error occurred.",
        "details": str(e)
    }
    # you could log the exception here with app.logger.error(str(e))
    return jsonify(response), 500

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
