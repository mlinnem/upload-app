from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Directory where uploaded files will be saved
UPLOAD_FOLDER = '/app/uploaded_files'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if the post request has the file part
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']
    
    if file.filename == '':
        return "No selected file"
    
    if file:
        # Save the file in the specified directory
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        return f"File {file.filename} uploaded successfully!"

if __name__ == "__main__":
    app.run(debug=True)
