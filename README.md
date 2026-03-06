# 🌱 AgriPulse – Precision Agriculture AI Dashboard

AgriPulse is a lightweight AI-powered web application designed to help farmers and agricultural analysts evaluate soil health and make smarter crop decisions.

The system analyzes soil nutrient values such as Nitrogen (N), Phosphorus (P), Potassium (K), and pH level to provide crop suitability insights and support sustainable farming practices.

---

## 🚜 Problem Statement

Farmers often struggle to determine the best crops for their soil conditions. Without proper soil analysis, this can lead to:

* Low crop yield
* Excess fertilizer usage
* Soil degradation
* Financial losses

AgriPulse helps solve this problem by providing **instant soil analysis and crop recommendations** using simple inputs or bulk datasets.

---

## ✨ Features

### 1️⃣ Manual Soil Entry

Users can manually enter soil parameters:

* Nitrogen (N)
* Phosphorus (P)
* Potassium (K)
* pH Level

The system analyzes the soil health and provides insights.

---

### 2️⃣ Bulk CSV Dataset Upload

Researchers or agricultural analysts can upload a CSV dataset containing multiple soil records.

This allows:

* Batch soil analysis
* Large-scale soil health evaluation
* Dataset processing for agricultural insights

---

### 3️⃣ Crop Selection

Users can select crops such as:

* Tomato 🍅
* Wheat 🌾
* Rice 🌾
* Corn 🌽

The system evaluates soil compatibility for the selected crop.

---

## 🧠 Technology Stack

**Frontend**

* HTML
* CSS

**Backend**

* Python
* Flask

**Data Processing**

* Pandas

**Deployment Environment**

* Replit

---

## 🏗 Project Structure

```
AgriPulse-Precision-Agriculture
│
├── app.py                 # Flask server
├── processor.py           # CSV dataset processing
├── agripulse_logic.py     # Soil analysis logic
├── requirements.txt       # Python dependencies
│
├── templates
│   └── index.html         # Web interface
│
└── README.md
```

---

## ⚙️ Installation & Running Locally

1. Clone the repository

```
git clone https://github.com/your-username/AgriPulse-Precision-Agriculture.git
```

2. Install dependencies

```
pip install -r requirements.txt
```

3. Run the application

```
python app.py
```

4. Open in browser

```
http://localhost:5000
```

---

## 📊 Example Soil Inputs

| N  | P  | K  | pH  |
| -- | -- | -- | --- |
| 50 | 40 | 40 | 6.5 |
| 70 | 50 | 60 | 6.8 |
| 30 | 20 | 25 | 5.5 |

---

## 🌍 Impact

AgriPulse helps support:

* Sustainable agriculture
* Data-driven farming
* Soil health awareness
* Efficient fertilizer use

---

## 🚀 Future Improvements

* AI crop recommendation system
* Soil health score
* Fertilizer suggestion engine
* Satellite soil monitoring integration
* Farmer mobile application

---

## 👨‍💻 Author

Developed for agricultural innovation and smart farming initiatives.
