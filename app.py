from flask import Flask, request, jsonify
import base64
import re
import os

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_selfie():
    data = request.get_json()
    image_data = data['image']

    # Decode the base64 image string and remove the header (data:image/png;base64,)
    image_data = re.sub('^data:image/.+;base64,', '', image_data)
    image_bytes = base64.b64decode(image_data)

    # Save the selfie as an image file
    save_path = os.path.join('uploads', 'selfie.png')  # Make sure 'uploads' directory exists
    with open(save_path, 'wb') as f:
        f.write(image_bytes)

    return jsonify({'message': 'Selfie uploaded and saved successfully'})

if __name__ == '__main__':
    app.run(debug=True)
