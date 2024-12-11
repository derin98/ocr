from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def health_check():
    return jsonify({
        "message": "Server is up and running",
        "result": {
            "version": "0.0.1.0",
            "description": "Image recognization application"
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
