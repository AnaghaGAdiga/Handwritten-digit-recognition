from flask import Flask, request, render_template, send_from_directory
from pyngrok import ngrok
import tensorflow as tf
import numpy as np
from PIL import Image
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

model = tf.keras.models.load_model("mnist_digit_recognition_model.h5")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files.get("file")
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)
        if file:
            image = Image.open(file)
            image = image.convert("L")
            image = image.resize((28, 28))
            image_array = np.array(image)

            if image_array.mean() > 127:
                image_array = np.invert(image_array)

            image_array = image_array / 255.0
            image_array = image_array.reshape(1, 28, 28)

            prediction = model.predict(image_array)
            predicted_digit = np.argmax(prediction)

            return f'''
                <html><head>
                <style>
                body {{
                    background-image: url("https://media.istockphoto.com/id/1281736074/vector/abstract-geometric-pattern-background.jpg?s=612x612&k=20&c=rTHAuJPGgbaGZCDh6PAoVkJr3mTvn5WppwDHAPfNgoU=");
                    background-size: cover; color: black;
                    font-family: Arial; text-align: center;
                }}
                </style></head>
                <body>
                    <h1>Predicted Digit: {predicted_digit}</h1>
                    <img src="/uploads/{file.filename}" alt="Uploaded Image">
                </body></html>
            '''
    return render_template("index.html")

@app.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == "__main__":
    public_url = ngrok.connect(5000)
    print(" * ngrok URL:", public_url)
    app.run(port=5000)
