KCET ML Full-Stack Predictor & College Recommendation Platform

An end-to-end, cloud-ready Machine Learning platform that predicts KCET ranks and recommends eligible engineering colleges using a scalable full-stack architecture.

This project demonstrates real-world ML system design, clean frontend/backend separation, and production-ready engineering practices, built with the same architectural principles used in modern SaaS applications.

Why This Project Stands Out

✅ End-to-End ML System — not just a notebook
✅ Clean Frontend–Backend Separation
✅ API-driven Architecture (FastAPI)
✅ Cloud-Deployable & Scalable
✅ Production-ready code structure
✅ Real dataset & real admission logic

This is not a toy project.
It mirrors how ML products are built and deployed in industry.

Problem Statement

Students appearing for KCET (Karnataka Common Entrance Test) struggle to:

Estimate their rank from marks

Identify realistic college options

Filter colleges by branch, location, and type

This platform solves the problem by:

Predicting KCET rank using a trained ML model

Recommending eligible colleges using historical cutoff data

Providing an intuitive UI for decision-making


🏗️ System Architecture

┌──────────────────┐        HTTP/JSON        ┌──────────────────────────┐
│  Streamlit UI    │  ───────────────────▶  │   FastAPI Backend        │
│  (Frontend)      │                        │  (ML + Business Logic)   │
└──────────────────┘                        └──────────────────────────┘
                                                     │
                                                     ▼
                                                     
                                            ML Model + College Dataset
                                            

Design Principles Used

Separation of Concerns

Stateless APIs

Single Source of Truth

Scalable & Cloud-friendly

🧪 Machine Learning Details
Model Pipeline

Feature engineering from KCET + Board marks

Normalization using StandardScaler

Supervised regression model

Post-prediction bias adjustment for real-world accuracy

Input Features

KCET score (normalized)

Board score (normalized)

Exam year

Total candidates appeared

Output

Predicted KCET rank

Why This Matters

This pipeline reflects real exam dynamics, not just raw regression.

🎓 College Recommendation Engine

Uses historical cutoff data (GM category)

Robust branch matching (handles naming variations)

Supports filters:

Branch

Location

College type

Returns only realistically achievable colleges

🧩 Tech Stack
Frontend

Streamlit

Pure UI layer (no ML or data logic)

Backend

FastAPI

RESTful API design

Pydantic validation

Scikit-learn integration

Machine Learning

Python

Scikit-learn

Pandas

NumPy

Data

Real KCET college cutoff dataset

Cleaned and normalized

Cloud & DevOps Ready

Environment-agnostic paths

Docker-friendly structure

Stateless backend design

kcet-ml-fullstack-predictor/

│

├── backend/

│   ├── backend.py              # FastAPI app

│   ├── models/

│   │   ├── model.pkl

│   │   └── scale.pkl

│   └── data/

│       └── Colleges.xlsx

│

├── frontend/

│   └── frontend.py             # Streamlit UI (pure frontend)

│

├── README.md

├── requirements.txt

└── .gitignore



⚙️ Running the Project Locally
1️⃣ Start Backend
uvicorn backend:app --reload


Backend runs at:

http://127.0.0.1:8000


Swagger docs:

http://127.0.0.1:8000/docs

2️⃣ Start Frontend
streamlit run frontend.py

Frontend runs at:

http://localhost:8501

🔗 API Endpoints

Method	Endpoint	Description
POST	/predict	Predict KCET rank
GET	/filters	Fetch filter options
POST	/recommandation/	Get college recommendations

☁️ Cloud Deployment Strategy

This project is designed for independent deployment:

Backend

Render

Railway

AWS EC2 / ECS

Docker container

Frontend

Streamlit Cloud

Vercel (via API proxy)

Custom VM

Frontend and backend can scale independently.

🔐 Production Considerations

Environment-based configuration

API validation with Pydantic

Stateless request handling

Clean error propagation

🧪 What This Project Demonstrates

✔ ML model integration into production
✔ Full-stack application design
✔ API-driven architecture
✔ Data engineering fundamentals
✔ Cloud-ready mindset
✔ Real-world problem solving

📈 Future Enhancements

Rank confidence intervals

Category-based cutoffs

Authentication & user profiles

Advanced ML models

CI/CD pipeline
