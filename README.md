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


## 2018-05-29 result

- Binary File I/O (Rendering)

```java
            try {
                this.writer = new PrintWriter(this.out);
                File f = new File(file_static_path + this.request_path);
                long flen = f.length();
                this.response.putHeader("Content-Length", Long.toString(flen));
                this.response.putHeader("Cache-Control","no-cache");

                String res = this.response.set();
                this.writer.append(res);
                this.writer.flush();

                byte[] b = new byte[MAXLEN];
                FileInputStream fis = new FileInputStream(file_static_path + this.request_path);
                int len = fis.read(b,0,MAXLEN);
                while (len != -1) {
                    this.out.write(b, 0, len);
                    len = fis.read(b);
                }

                this.out.flush();
                this.writer.close();
                fis.close();
            } catch (FileNotFoundException e) {
                this.sendFobiddenMessage();
            }
```

- Binary File I/O upload & download (Multipart)

```java
            try {
                this.writer = new PrintWriter(this.out);
                File f = new File(file_static_path + this.request_path);
                long flen = f.length();
                this.response.putHeader("Content-Type", "multipart/form-data; boundary=december");
                this.response.putHeader("Content-Length", Long.toString(flen));
                this.response.putHeader("Cache-Control","no-cache");
                String res = this.response.set();
                this.writer.append(res);
                this.writer.flush();
                
                byte[] b = new byte[MAXLEN];
                FileInputStream fis = new FileInputStream(file_static_path + this.request_path);
                int len = fis.read(b,0,MAXLEN);
                while (len != -1) {
                    this.out.write(b, 0, len);
                    len = fis.read(b);
                }
                
                this.out.flush();
                this.writer.close();
                fis.close();
            } catch (FileNotFoundException e) {
                this.sendFobiddenMessage();
            }
```
