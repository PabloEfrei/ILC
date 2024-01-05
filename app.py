from flask import Flask, render_template, request, jsonify #choose flask over fastAPI as it is included in Google Collab
import tensorflow as tf
import cv2
import numpy as np
import os
os.getcwd()

app = Flask(__name__)

# Load the model
model = tf.keras.models.load_model('EAP_Net.h5')

# Define the classes for binary classification
classes = {
    0: 'Buildings',
    1: 'Forest',
    2: 'Glacier',
    3: 'Mountain',
    4: 'Sea',
    5: 'Street'
}

@app.route('/')
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        return str(e), 500


@app.route('/classify', methods=['POST'])
def classify_image():
    try:
        # Get image data from the request
        if 'image' in request.files:
            image_data = request.files['image'].read()
            image = cv2.imdecode(np.frombuffer(image_data, np.uint8), cv2.IMREAD_COLOR)
        else:
            return jsonify({'error': 'No image file provided'}), 400

        # Preprocess the image
        image = cv2.resize(image, (150, 150))
        image = image / 255.0       
        image = image.reshape((1, 150, 150, 3))  # Ensure the image has 3 channels

        # Make predictions
        predictions = model.predict(image)
        predicted_class = int(np.argmax(predictions[0]))

        # Return the result
        return jsonify({'predicted_class': predicted_class, 'class_name': classes[predicted_class]})
    except Exception as e:
        #return jsonify({'error': str(e)})
        return jsonify({'error': str(e), 'request_data': request.data.decode('utf-8'), 'headers': dict(request.headers)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)