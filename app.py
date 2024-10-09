from flask import Flask, render_template, request
import ibm_boto3
from ibm_botocore.client import Config, ClientError
import os

app = Flask(__name__)

# IBM Cloud Object Storage configuration
COS_ENDPOINT = 'https://control.cloud-object-storage.cloud.ibm.com/v2/endpoints'  # Example endpoint, adjust as necessary
COS_API_KEY_ID = 'KXYPDmNqPTVZogul31bFLG3-_U24qQaAjNnQaWxzpjfF'  # Replace with your IBM COS API key
COS_INSTANCE_CRN = 'crn:v1:bluemix:public:cloud-object-storage:global:a/0bb4d59c58f057ca240dd82f9bf0ca02:e6782f1a-cbf0-4a2e-82cc-1dda2edb2fe8::'  # Replace with your service instance CRN
COS_BUCKET_NAME = 'bucket-for-upload-app'  # Replace with your bucket name
COS_REGION = 'us-south'  # Replace with your COS region

# Create COS client
cos = ibm_boto3.client('s3',
    ibm_api_key_id=COS_API_KEY_ID,
    ibm_service_instance_id=COS_INSTANCE_CRN,
    config=Config(signature_version='oauth'),
    endpoint_url=COS_ENDPOINT
)

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
        try:
            # Upload the file to the IBM Cloud Object Storage bucket
            cos.upload_fileobj(
                file,
                COS_BUCKET_NAME,
                file.filename
            )
            return f"File {file.filename} uploaded to Cloud Object Storage successfully!"
        
        except ClientError as e:
            print(f"Error: {e}")
            return f"File upload failed {e}"
    
if __name__ == "__main__":
    app.run(debug=True)
