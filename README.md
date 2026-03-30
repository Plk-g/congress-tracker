# 🏛️ Congress Tracker

> Making U.S. legislation transparent, searchable, and accessible to everyone.

![Status](https://img.shields.io/badge/status-in%20development-purple)
![Python](https://img.shields.io/badge/python-3.11-blue)
![Flask](https://img.shields.io/badge/backend-Flask-lightgrey)
![Firebase](https://img.shields.io/badge/database-Firebase-orange)
![React](https://img.shields.io/badge/frontend-React-61DAFB)
![License](https://img.shields.io/badge/license-MIT-green)

---

## 📌 Overview

Congress Tracker is a full-stack civic-tech web application that aggregates and visualizes U.S. legislative data from the official [Congress.gov API](https://api.congress.gov/). The goal is to lower the barrier to understanding what Congress is doing — for students, journalists, researchers, and engaged citizens.

Built as part of the **LeetCode Bootcamp** (Spring 2025) by a team of NYU students.

---

## ✨ Features

| Feature | Status |
|---|---|
| Legislative Dashboard — search & filter bills | 🔄 In Progress |
| Member Profiles — sponsorship & voting records | 🔄 In Progress |
| Firebase Authentication — user accounts | 🔄 In Progress |
| Bill Outcome Prediction — Decision Tree model | 🔄 In Progress |
| Data Visualizations — legislative trends | 📅 Planned |
| Notifications — alerts for tracked bills | 📅 Planned |
| Community Comments — discuss bills | 📅 Planned |

---

## 🧱 Tech Stack

**Backend**
- Python 3.11 + Flask — REST API server
- Congress.gov API — live legislative data
- Firebase Firestore — NoSQL database

**Frontend**
- React.js — component-based UI
- Chart.js — data visualizations

**Auth & Infra**
- Firebase Authentication
- Vercel (frontend deployment)
- Railway (backend deployment)

**Machine Learning**
- scikit-learn — Decision Tree Classifier
- pandas + NumPy — data processing

---

## 🗂️ Project Structure
```
congress-tracker/
├── backend/
│   ├── app.py               # Flask entry point & route definitions
│   ├── routes/
│   │   ├── bills.py         # Bill search & detail endpoints
│   │   └── members.py       # Member profile endpoints
│   ├── models/
│   │   └── decision_tree.py # Bill outcome prediction model
│   ├── firebase_config.py   # Firebase initialization
│   └── requirements.txt
├── frontend/                # React app (coming Week 5)
├── notebooks/               # EDA & model training notebooks
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- A free [Congress.gov API key](https://api.congress.gov/sign-up/)
- A Firebase project with Firestore enabled

### Installation
```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/congress-tracker.git
cd congress-tracker/backend

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# → Add your CONGRESS_API_KEY and Firebase credentials to .env

# Run the development server
python app.py
```

### API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/bills` | Fetch recent bills (paginated) |
| `GET` | `/bill/<congress>/<type>/<number>` | Get bill details |
| `GET` | `/members` | Fetch Congress members |
| `GET` | `/member/<id>` | Get member profile |

---

## 🤖 ML Model

We train a **Decision Tree Classifier** to predict whether a bill is likely to pass based on:

- Sponsor's party affiliation
- Bill type (HR, S, HJRes, etc.)
- Number of co-sponsors
- Referring committee
- Historical passage rate by subject area

> Model training notebooks are available in `/notebooks`.

---

## 👥 Team

| Name | GitHub |
|---|---|
| Palak Gupta | [@pg2820](https://github.com/pg2820) |
| Nitin Mohan | [@nm5029](https://github.com/nm5029) |
| Neil Noronha | [@nn685](https://github.com/nn685) |
| Natalia Volkova | [@nv2170](https://github.com/nv2170) |
| Cameron Bedard | [@cb5179](https://github.com/cb5179) |

---

## 📅 Roadmap

- [x] Week 1–2: API exploration & environment setup
- [x] Week 3: Flask backend & Firebase schema
- [ ] Week 5–6: React frontend & Firebase Auth
- [ ] Week 7: Decision Tree model & data visualizations
- [ ] Week 8: Deployment & final testing
- [ ] Week 9: Final presentation

---

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgements

- [Library of Congress — Congress.gov API](https://api.congress.gov/)
- [LeetCode Bootcamp](https://leetcode.com/) — Spring 2025
- NYU for the collaboration space
```

---

## 📁 Also create these two small files:

**.env.example** (commit this, NOT your real .env)
```
CONGRESS_API_KEY=your_api_key_here
FIREBASE_PROJECT_ID=your_project_id
FIREBASE_PRIVATE_KEY=your_private_key
FIREBASE_CLIENT_EMAIL=your_client_email
```

**requirements.txt**
```
flask==3.0.0
requests==2.31.0
python-dotenv==1.0.0
firebase-admin==6.4.0
scikit-learn==1.4.0
pandas==2.2.0
numpy==1.26.4
