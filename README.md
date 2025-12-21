#  KCET Rank Prediction & College Recommendation Platform

An **end-to-end, production-ready Machine Learning full-stack application** that predicts **KCET ranks** and recommends **realistic engineering colleges** using historical cutoff data.

This project mirrors how **real ML products are built, containerized, and deployed in industry**, not just how models are trained in notebooks.

##  Why This Project Stands Out

✔ End-to-End ML System (Model → API → UI)

✔ Clean Frontend–Backend Separation

✔ API-Driven Architecture (FastAPI)

✔ Real Admission Logic

✔ Dockerized & Cloud-Ready

✔ Production-Grade Project Structure

Problem Statement

Students appearing for KCET (Karnataka Common Entrance Test)** struggle to:

* Estimate their expected rank** from exam marks
* Identify **realistic college options**
* Filter colleges by **branch, location, and type**

This platform solves these problems by:

* Predicting KCET rank using a trained ML model
* Recommending eligible colleges using historical cutoff data
* Providing a simple, intuitive UI for decision-making


Design Principles Used

* Separation of Concerns
* Stateless APIs
* API-First Design
* Scalable & Cloud-Friendly Architecture


Machine Learning Pipeline

Features Used

* KCET score (normalized)
* Board score (normalized)
* Exam year
* Total candidates appeared

Pipeline

1. Feature Engineering
2. Standardization using `StandardScaler`
3. Supervised Regression Model
4. Post-prediction bias correction for real-world accuracy

Output

Predicted KCET Rank**

The pipeline reflects real exam dynamics, not just raw regression output.


College Recommendation Engine

* Uses **real historical cutoff data (GM category)**
* Intelligent branch name matching (handles variations)
* Filters supported:

  * Branch
  * Location
  * College type
* Returns **only realistically achievable colleges**

Tech Stack

### Backend

* Python 3.11
* FastAPI
* Pydantic
* Scikit-learn
* Pandas, NumPy

### Frontend

* Streamlit
* Requests (API communication)

### DevOps & Deployment

* Docker & Docker Compose
* Environment-agnostic paths
* Stateless service design

📁Project Structure

kcet-rank-college-advisor-platform/

│

├── Backend/

│   ├── backend.py

│   ├── Dockerfile

│   ├── requirements.txt

│   ├── models/

│   │   ├── model.pkl

│   │   └── scale.pkl

│   ├── data/

│   │   └── Colleges.xlsx

│   └── utils/

│       └── matches.py

│

├── Frontend/

│   ├── frontend.py

│   ├── Dockerfile

│   └── requirements.txt

├── docker-compose.yml

├── .gitignore

└── README.md

🔗 API Endpoints

| Method | Endpoint          | Description           |
| ------ | ----------------- | --------------------- |
| POST   | `/predict`        | Predict KCET rank     |
| GET    | `/filters`        | Fetch filter options  |
| POST   | `/recommendation` | Get eligible colleges |


## 🐳 Dockerization (Production-Ready)

This project is **fully Dockerized** with **independent frontend and backend containers**.

### Why Docker?

* Consistent environments
* Easy cloud deployment
* Independent scaling
* No “works on my machine” issues

## ▶️ Run the Project Using Docker (Recommended)

### Prerequisites

* Docker
* Docker Compose


```bash
cd Backend
python -m venv myenv
source myenv/bin/activate  # Windows: myenv\Scripts\activate
pip install -r requirements.txt
uvicorn backend:app --reload

### Frontend

```bash
cd Frontend
pip install -r requirements.txt
streamlit run frontend.py

## ☁️ Cloud Deployment Strategy

### Backend

* Render
* Railway
* AWS EC2 / ECS
* Any Docker-based platform

### Frontend

* Streamlit Cloud
* Vercel (via API proxy)
* Docker container

Frontend and backend can be **scaled independently**.


##  Production Considerations

✔ Stateless backend design
✔ Environment-based configuration
✔ API validation using Pydantic
✔ Clean error handling
✔ Minimal Docker images


##  Future Enhancements

* Rank confidence intervals
* Category-based cutoffs
* Authentication & user profiles
* Advanced ML models
* CI/CD pipeline (GitHub Actions)


##  What This Project Demonstrates

✔ Real-world ML deployment
✔ Full-stack system design
✔ API-driven architecture
✔ Docker & DevOps fundamentals
✔ Clean, maintainable codebase
✔ Industry-ready engineering minds.
