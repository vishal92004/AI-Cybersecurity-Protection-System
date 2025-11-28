# System Design Document

## 1. Overview
The AI-Based Cybersecurity Support System is designed to detect phishing URLs, scam patterns, cyber risks and provide real-time alerts to protect users.  
It uses lightweight AI models, rule-based heuristics, and threat-intelligence datasets to help users avoid digital fraud.

---

## 2. High-Level Architecture
User → App/Frontend → API (Flask) → AI Engine → Threat Database → Alert System → Output to User

---

## 3. Components

### **Frontend (Optional)**
- Simple UI built with Flutter or React
- Input box for checking links
- Dashboard for risk scores

### **Backend**
- Flask Python API
- Endpoints: `/health`, `/check-url`

### **AI Engine**
- Rule-based suspicion scoring
- ML/NLP models (future upgrade)
- Keyword detection module
- HTTP safety check

### **Threat-Intelligence Layer**
- Sample phishing dataset
- External data sources (future)

### **Alert / Recommendation System**
- Provides:
  - Risk Score (0–100)
  - Explanation of risk factors
  - Recommended safe action

---

## 4. Data Flow Diagram (Text Form)
```
User Input
     ↓
Flask API (app.py)
     ↓
analyze_url() in phishing_detection.py
     ↓
Risk Score + Reason
     ↓
JSON Response to User
```

---

## 5. Future Enhancements
- Deep learning phishing classifier  
- SMS scam detection model  
- Cyberbullying detection (NLP)  
- Real-time browser extension  
- Multi-language cyber safety tips  

---

## 6. Conclusion
This system provides a foundational AI-based cybersecurity mechanism for safe internet usage and can be expanded into a complete security suite in future.
