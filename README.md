# test-to-send-or-recieve-image
This repo is only used to test sending or recieving image on flask framework

## 2018-05-02 result

```
# example

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/download/<filename>", methods=["GET"])
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename), 200
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug = True)
```


- Flask's "send_file()" and "send_from_directory()" is only useful, if you provide a link to be available to download file.
- This case is only available to download **the filename in UPLOAD_FOLDER** metioned **in url's rule**.
- Therefore, I'll make thread to send or recieve image-file.


## 2018-05-03 result
- Sending image file was success, but seding speed was very slow.
- I think that this situation was likely to occur by thread issue.
- If possible, I want to find another python module.
