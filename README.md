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

- To develop an accurate image classification model for identifying cattle and buffalo breeds.  
- To support farmers and livestock authorities with quick, automated breed recognition.  
- To build a scalable AI system that can later work offline via **TensorFlow Lite** or integrate with government platforms like **Bharat Pashudhan App (BPA)**.

---

## ⚙️ **Key Features**

✅ **AI-Powered Breed Detection** – Uses CNN / MobileNet / EfficientNet models for image-based prediction.  
✅ **Web Application Interface** – Upload an image and get instant breed name + confidence score.  
✅ **Indian Breed Dataset Focus** – Optimized for breeds like **Gir, Sahiwal, Murrah, Tharparkar**, etc.  
✅ **Optional Cloud Integration** – Can connect with the **BPA API** for automated record updates.  
✅ **Future-Ready Design** – Supports conversion to TensorFlow Lite for **mobile or offline** inference.  
✅ **User-Friendly UI** – Simple, intuitive, and accessible even in low-connectivity rural areas.

---

## 🏗️ **System Architecture**

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

## 🧩 **Tech Stack**

| Component | Technology Used |
|------------|----------------|
| **Frontend** | HTML, CSS, JavaScript / React.js |
| **Backend** | Python (Flask / FastAPI) |
| **AI Model** | TensorFlow / Keras (CNN, MobileNet, EfficientNet) |
| **Dataset** | Public cattle/buffalo breed datasets or custom dataset |
| **Cloud / Database** | Firebase / MongoDB / SQLite |
| **Version Control** | Git & GitHub |
| **Future Expansion** | TensorFlow Lite for mobile, BPA API Integration |

---

## 🧪 **Model Workflow**

1. **Dataset Collection** – Images of Indian cattle and buffalo breeds.  
2. **Preprocessing** – Image resizing, normalization, and augmentation.  
3. **Model Training** – CNN or MobileNet-based classifier trained on labeled data.  
4. **Evaluation** – Accuracy, confusion matrix, and F1-score metrics.  
5. **Deployment** – Model integrated into a Flask/React web app.  
6. **User Interaction** – Upload → Predict → Get Results instantly.  

---

## 🚀 **How to Run Locally**

### 🔸 Clone Repository
```bash
git clone https://github.com/<your-username>/PashuDrishti.git
cd PashuDrishti
```

### 🔸 Install Dependencies
```bash
pip install -r requirements.txt
```

### 🔸 Run Backend Server
```bash
python app.py
```

### 🔸 Run Frontend (if React-based)
```bash
npm install
npm start
```

Then open **http://localhost:3000** in your browser.

---

## 📈 **Future Enhancements**

- 📱 TensorFlow Lite integration for offline mobile prediction.  
- ☁️ API integration with **Bharat Pashudhan App (BPA)**.  
- 🛰️ GPS tagging and QR-based livestock tracking.  
- 📊 Dashboard for analytics, breed statistics, and health insights.  
- 🔊 Voice-based interaction for farmers in local languages.

---

## 💡 **Example Prediction**

| Image Input | Predicted Breed | Confidence |
|--------------|----------------|-------------|
| 🐄 Gir cow image | Gir | 96% |
| 🐃 Murrah buffalo image | Murrah | 94% |
| 🐄 Sahiwal cow image | Sahiwal | 92% |

---

## 👨‍💻 **Developed By**
**Mayank Kumar**  
*(Independent Developer – AI, ML, and Web Enthusiast)*  

📧 **Email:** [02mayankk@gmail.com](mailto:02mayankk@gmail.com)  
🌐 **GitHub:** [github.com/02mayankk](https://github.com/02mayankk)  

---

## 🐮 **Tagline**
> *“Smart Vision for Smarter Livestock – Empowering Farmers with AI.”*
