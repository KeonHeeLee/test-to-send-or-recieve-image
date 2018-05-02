from flask import Flask, jsonify, request
from util import util
from exception import exception

util = util()
exception = exception()

UPLOAD_FOLDER = 'upload'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/download", methods=["POST"])
def send_image():
    data = request.get_json()
    user = data["user"]
    reply = util.recieving_image_status(user=user)

    try:
        return jsonify(reply), 200

    except:
        return jsonify(exception.error(user=user)), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
