import os
import subprocess
from flask import Flask, render_template, request, jsonify
import base64
from PIL import Image
import io
from YOLO_V8_WebCam import process_captured_images  # Adjust import based on your file structure

app = Flask(__name__)

@app.route("/")
def index():
    # Render log in and sign up
    return render_template("index.html")

@app.route("/signup")
def signup():
    # Render signup page
    return render_template("signup.html")

@app.route("/home")
def home():
    # Render home page after login/signup
    return render_template("templates\home.html")

@app.route("/scanitem")
def scanitem():
    # Render the page for scanning items
    # Assume "cam.html" is the file for capturing images
    return render_template("cam.html")

@app.route('/capture', methods=['POST'])
def capture():
    data = request.get_json()
    image_data = data['image']
    # Remove the header from the base64 encoded string
    image_data = image_data.split(",")[1]
    image_bytes = base64.b64decode(image_data)
    image = Image.open(io.BytesIO(image_bytes))
    # Save the image or process it
    filepath = os.path.join('captured_images', 'captured_image.png')  # Ensure this directory exists
    image.save(filepath)

     # Process the saved image with YOLOv8
    yolov8_results = process_captured_images(filepath)
    print("YOLOv8 Results:", yolov8_results)

    #date
    print("Expiration Date:", expiryDate)
    
    
    return jsonify({'message': 'Image and expiration date received successfully!'})
    # image.save("captured_image.png")
    # # Respond back to the client
    # return jsonify({'message': 'Image captured and saved successfully!'})

if __name__ == "__main__":
    app.run(debug=True)
