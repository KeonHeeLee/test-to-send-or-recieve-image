from flask import Flask, jsonify, request, make_response, send_from_directory
from util import util
import exception

util = util()
ex = exception.exception()

UPLOAD_FOLDER = 'uploaded'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/message", methods=["POST"])
def send_image():
    data = request.get_json()
    user = data["user"]
    reply = util.recieving_image_status(user=user)

    try:
        return jsonify(reply), 200

    except:
        return jsonify(ex.error(user=user,flag=exception.SERVER_ERROR)),500

@app.route("/uploaded", methods=["POST"])
def upload_image():
    response = make_response()
    try:
        image = request.files['image']
        image.save(image.filename)
        response.status_code = 200
    except Exception as e:
        print(e)
        response.status_code = 415
    return response

@app.route("/download/<filename>", methods=["GET"])
def send_image_to_client(filename):
    try:
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename=filename)
    except:
        return jsonify(ex.error_nonfile(flag=exception.NON_EXISTENT_FILE)), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)