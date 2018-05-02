from flask import Flask, jsonify
from pi_screen import screen
import os

sc = screen()

UPLOAD_FOLDER = 'screenshot'
SUCCESS_MESSAGE = {"result" : True}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/image", methods=["POST"])
def get_image():
    filename = sc.send_image()
    try:
        return jsonify(SUCCESS_MESSAGE), 200

    except:
        os.remove(UPLOAD_FOLDER+"/"+filename)
        return filename, 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000, debug=True)
