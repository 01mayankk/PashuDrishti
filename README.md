# 🐮 PashuDrishti – AI-Based Cattle & Buffalo Breed Recognition

### Problem ID: 25004 – *Image-Based Breed Recognition for Cattle and Buffaloes (Beginner to Intermediate)*

---

## 🧠 **Overview**

**PashuDrishti** is an AI-powered web application designed to recognize the breed of cattle and buffaloes from images.
By leveraging **deep learning** and **computer vision**, it helps farmers, veterinarians, and field workers identify animal breeds instantly, improving livestock management and record accuracy.

The system analyzes visual traits such as **coat color**, **horn shape**, **body structure**, and **facial features** to determine the breed and confidence score.
Initially developed as a **web-based model**, it is later planned to be integrated into **mobile or offline** systems for real-time field use.

---

## 🎯 **Objectives**

* To develop an accurate image classification model for identifying cattle and buffalo breeds.
* To support farmers and livestock authorities with quick, automated breed recognition.
* To build a scalable AI system that can later work offline via **TensorFlow Lite** or integrate with government platforms like **Bharat Pashudhan App (BPA)**.

---

## ⚙️ **Key Features**

✅ **AI-Powered Breed Detection** – Uses CNN / MobileNet / EfficientNet models for image-based prediction.
✅ **Web Application Interface** – Upload an image and get instant breed name + confidence score.
✅ **Indian Breed Dataset Focus** – Optimized for breeds like **Gir, Sahiwal, Murrah, Tharparkar**, etc.
✅ **Optional Cloud Integration** – Can connect with the **BPA API** for automated record updates.
✅ **Future-Ready Design** – Supports conversion to TensorFlow Lite for **mobile or offline** inference.
✅ **User-Friendly UI** – Simple, intuitive, and accessible even in low-connectivity rural areas.

---

## 🧩 **System Architecture**

```
[User Uploads Image]
        ↓
[Web Interface (React/HTML)]
        ↓
[Backend API – Flask / FastAPI / Node.js]
        ↓
[AI Model – CNN / MobileNet / EfficientNet]
        ↓
[Predicted Breed + Confidence Score]
        ↓
[Display on Web Dashboard / Optional Sync with BPA]
```

---

## 🧠 **Model Workflow**

1. **Dataset Collection** – Images of Indian cattle and buffalo breeds.
2. **Preprocessing** – Image resizing, normalization, and augmentation.
3. **Model Training** – CNN or MobileNet-based classifier trained on labeled data.
4. **Evaluation** – Accuracy, confusion matrix, and F1-score metrics.
5. **Deployment** – Model integrated into a Flask/React web app.
6. **User Interaction** – Upload → Predict → Get Results instantly.

---

## ⚙️ **Software Requirements**

### 🖥️ Frontend

* HTML5, CSS3, JavaScript / React.js
* Axios / Fetch API for backend communication
* TailwindCSS / Bootstrap for quick UI design

### 🔧 Backend

* Python 3.10+
* Flask / FastAPI (for REST API)
* TensorFlow / Keras (for CNN model)
* OpenCV, Pillow, NumPy (for preprocessing)
* joblib / pickle (for saving model weights)

### 🧠 AI/ML Libraries

* TensorFlow (≥2.10)
* Keras
* scikit-learn
* matplotlib / seaborn

### 🗄️ Database (Optional)

* SQLite (local) / MongoDB / Firebase (cloud)

### 🌐 Deployment Tools

* Render, Hugging Face Spaces, or Streamlit Cloud
* TensorFlow Lite (future mobile version)

---

## 💾 **Dataset Requirements**

| Requirement       | Description                                            |
| ----------------- | ------------------------------------------------------ |
| **Image Dataset** | High-quality images of Indian cattle & buffalo breeds  |
| **Breed Labels**  | Gir, Sahiwal, Murrah, Tharparkar, Red Sindhi, etc.     |
| **Sources**       | Public datasets (Kaggle, NDDB, ICAR) or custom dataset |
| **Image Format**  | JPG / PNG, ideally 224x224 or 256x256 resolution       |
| **Augmentation**  | Rotation, flip, brightness, contrast adjustments       |

---

## 🔋 **Hardware Requirements**

| Component                       | Requirement                             |
| ------------------------------- | --------------------------------------- |
| **Development Machine**         | Laptop/PC with ≥8 GB RAM, 4-core CPU    |
| **GPU (Optional)**              | NVIDIA GPU for faster training          |
| **Mobile/Camera Device**        | To test real-world image capture        |
| **(Optional)** IoT Camera Setup | For future automated livestock scanning |

---

## 🧩 **Suggested File Structure**

```
PashuDrishti/
│
├── backend/
│   ├── app.py
│   ├── model/
│   │   ├── breed_model.h5
│   │   ├── labels.json
│   └── utils/
│       ├── preprocess.py
│
├── frontend/
│   ├── index.html
│   ├── styles.css
│   ├── script.js
│
├── dataset/
│   ├── train/
│   ├── test/
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

## 📦 **Example requirements.txt**

```
Flask==3.0.2
tensorflow==2.16.1
keras==3.1.1
numpy==1.26.4
pillow==10.2.0
opencv-python==4.9.0.80
scikit-learn==1.5.2
matplotlib==3.9.2
seaborn==0.13.2
gunicorn==21.2.0
```

---

## 📈 **Future Enhancements**

* 📱 TensorFlow Lite integration for offline mobile prediction
* ☁️ API integration with **Bharat Pashudhan App (BPA)**
* 🛰️ GPS tagging and QR-based livestock tracking
* 📊 Analytics dashboard for breed insights
* 🔊 Voice-based feedback in local languages

---

## 💡 **Example Prediction**

| Image Input             | Predicted Breed | Confidence |
| ----------------------- | --------------- | ---------- |
| 🐄 Gir cow image        | Gir             | 96%        |
| 🐃 Murrah buffalo image | Murrah          | 94%        |
| 🐄 Sahiwal cow image    | Sahiwal         | 92%        |

---

## 👨‍💻 **Developed By**

**Mayank Kumar**
*(Independent Developer – AI, ML, and Web Enthusiast)*

📧 **Email:** [02mayankk@gmail.com](mailto:02mayankk@gmail.com)
🌐 **GitHub:** [github.com/02mayankk](https://github.com/02mayankk)

---

## 🐮 **Tagline**

> *“Smart Vision for Smarter Livestock – Empowering Farmers with AI.”*
