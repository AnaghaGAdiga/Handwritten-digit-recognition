# 🧠 Digit Recognition Web App with Flask + TensorFlow

This is a web application that predicts handwritten digits using a deep learning model trained on the MNIST dataset. Built with **Flask**, powered by **TensorFlow**, and accessible via **Ngrok**.

<br>

---

## 🚀 Features

- Upload an image of a handwritten digit (0–9)
- Model predicts the digit with high accuracy
- Image is preprocessed (grayscale, resized, normalized)
- Web interface designed using basic HTML/CSS
- Ngrok used to expose app to the internet

---

## 🛠️ Tech Stack

- Python
- Flask
- TensorFlow / Keras
- Pillow (image handling)
- Ngrok (for tunneling)
- HTML + CSS (frontend)

---

## 📂 Project Structure

```

digit-recognition-flask/
│
├── app.py                        # Main Flask app
├── mnist\_digit\_recognition\_model.h5  # Trained MNIST model
├── uploads/                     # Uploaded files (auto-created)
├── templates/
│   └── index.html               # Web UI
├── requirements.txt             # Python dependencies
└── .gitignore

```

---

## 🧪 Demo (via Ngrok)

When you run the app, you’ll get an output like:

```

* ngrok URL: [https://1234-56-78-90-12.ngrok-free.app](https://1234-56-78-90-12.ngrok-free.app) -> [http://localhost:5000](http://localhost:5000)

````

Visit that public URL to access your app!

---

## 🧰 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YourUsername/digit-recognition-flask.git
cd digit-recognition-flask
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add Ngrok Auth Token (replace with your actual token)

```bash
ngrok authtoken <your_ngrok_token>
```

### 4. Run the app

```bash
python app.py
```

---

## 🎯 Sample Predictions

* Upload an image like this:

  ![sample\_digit](https://upload.wikimedia.org/wikipedia/commons/2/27/MnistExamples.png)

* Get output like:

  ```
  Predicted Digit: 7
  ```

---

## 📌 Notes

* The model used is a `.h5` file trained on MNIST using TensorFlow.
* You can replace it with your own trained model if needed.

---

## 💡 Future Improvements

* Deploy to cloud (Render / Heroku / AWS)
* Add REST API endpoint
* Add confidence/probability visualization
* Drag and drop image upload
* Support for mobile responsiveness

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙌 Acknowledgements

* [MNIST Dataset](http://yann.lecun.com/exdb/mnist/)
* [Flask](https://flask.palletsprojects.com/)
* [TensorFlow](https://www.tensorflow.org/)
* [Ngrok](https://ngrok.com/)

---

### 👩‍💻 Created by Anagha Adiga

```

---

Let me know if you'd like:
- A `LICENSE` file
- A sample `mnist_digit_recognition_model.h5` (training notebook)
- The ZIP file of this full repo for download

Want me to auto-generate and push this structure to your GitHub repo?
```
