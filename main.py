import os
from flask import Flask, redirect, request, send_file
from google.cloud import storage
from google.cloud import storage

os.makedirs('files', exist_ok = True)
storage_client = storage.Client()
BUCKET_NAME = "cnd_proj1_bucket1"

app = Flask(__name__)

@app.route('/')
def index():
    index_html="""
<form enctype="multipart/form-data" action="/upload" method="post">
  <div>
    <label for="file">Choose file to upload</label>
    <input type="file" id="file" name="form_file" accept="image/jpeg"/>
  </div>
  <div>
    <button>Submit</button>
  </div>
</form>
<ul>"""    

    for file in list_files():
        img_path = f"https://storage.cloud.google.com/{BUCKET_NAME}/{file}"
        index_html += f"<li><a href={img_path}>{file}</a></li>"

    index_html += "</ul>"
    return index_html

@app.route('/upload', methods=["POST"])
def upload():
    # Send File to bucket
    file = request.files.get('form_file')  # item name must match name in HTML form
    if not file or not file.filename:
      return "No file selected", 400

    local_path = os.path.join("./files", file.filename)

    file.save(local_path)

    bucket = storage_client.bucket(BUCKET_NAME)
    blob = bucket.blob(file.filename)
    blob.upload_from_filename(local_path)

    # os.remove(local_path)

    return redirect("/")

@app.route('/files')
def list_files():
    bucket = storage_client.bucket(BUCKET_NAME)
    blobs = bucket.list_blobs()

    jpegs = []
    for blob in blobs:
        if blob.name.lower().endswith(".jpeg") or blob.name.lower().endswith(".jpg"):
            jpegs.append(blob.name)
    
    return jpegs

@app.route('/files/<filename>')
def get_file(filename):
  path = os.path.join(BUCKET_NAME + '/', filename)
  bucket = storage_client.bucket(BUCKET_NAME)

  blob = bucket.blob(filename)
  blob.download_to_filename(path)

  return send_file(path)

if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)