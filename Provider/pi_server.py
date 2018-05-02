from flask import Flask, jsonify
from pi_screen import screen
import os, threading

sc = screen()

UPLOAD_FOLDER = 'screenshot'


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/image", methods=["POST"])
def get_image():
    filename = sc.copy_image()

    print("copy complete.")

    sender = threading.Thread(target=sc.send_image_to_server, args=(filename,))
    sender.start()

    SUCCESS_MESSAGE = {"path": filename}
    try:
        return jsonify(SUCCESS_MESSAGE), 200

    except:
        os.remove(path="screenshot/"+filename)
        return "fail", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000, debug=True)