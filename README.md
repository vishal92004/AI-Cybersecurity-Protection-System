# 🔐 AI-Cybersecurity-Protection-System
An AI-driven lightweight cybersecurity solution designed to detect phishing links, scam patterns, and risky URLs in real time — built to support digital safety for youth, students, and first-time internet users.

---

## 🚀 Features
- 🔎 Real-time phishing URL detection  
- 🧠 AI + Rule-based scam prediction engine  
- ⚠️ Risk scoring (0–100) with clear explanation  
- 🕵️ HTTP safety & suspicious keyword check  
- 📊 Sample phishing dataset included  
- 🔧 Simple Flask API (easy to test & extend)  
- 📁 Clean project structure for hackathons & judges  

---

## 🧠 Tech Stack
- **Python**
- **Flask** (API)
- **NLP / ML extension-ready**
- **Pandas / Numpy**
- **PyTorch**
- **Transformers**
- **CSV dataset**

---

## 📁 Project Structure
```
AI-Cybersecurity-Protection-System/
├── src/
│   ├── app.py
│   └── phishing_detection.py
├── docs/
│   └── system_design.md
├── data/
│   └── sample_phishing_links.csv
├── tests/
│   └── test_phishing.py   (optional)
├── requirements.txt
├── .gitignore
└── LICENSE
```

---

## ▶ Running Locally (Quick Start)

### 1️⃣ Create & activate virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 2️⃣ Install dependencies:
```bash
pip install -r requirements.txt
```

### 3️⃣ Start the backend API:
```bash
python src/app.py
```

### 4️⃣ Test the API (health check):
```bash
curl http://localhost:5000/health
```

### 5️⃣ Test phishing detection:
```bash
curl -X POST http://localhost:5000/check-url \
  -H "Content-Type: application/json" \
  -d '{"url":"http://verify-your-bank-login.com"}'
```

### 6️⃣ Run unit tests (Optional but recommended):
```bash
pip install pytest
pytest -q
```

---

## 🗂 Dataset
The project includes a sample CSV dataset containing phishing and safe URLs, located in:

```
data/sample_phishing_links.csv
```

This helps demonstrate the detection logic and model expansion capability.

---

## 🏗 System Design
System design details are available in:

```
docs/system_design.md
```

Includes:
- High-level architecture  
- Component explanation  
- Data flow diagram  
- Future enhancements  

---

## 🔮 Future Enhancements
- Deep learning–based phishing classifier  
- SMS scam detection  
- Browser extension for real-

