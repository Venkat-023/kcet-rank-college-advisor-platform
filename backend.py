from fastapi import FastAPI
import pickle
import pandas as pd
import numpy as np
from pydantic import BaseModel
from utils.matches import matches_branch

with open('C:\\Users\\admin\\Desktop\\Kcet Predictor\\models\\model.pkl','rb') as m:
    model=pickle.load(m)
with open('C:\\Users\\admin\\Desktop\\Kcet Predictor\\models\\scale.pkl','rb') as s:
    scaler=pickle.load(s)

app=FastAPI(title='Kcet Rank Predictor')

df_colleges=pd.read_excel('C:\\Users\\admin\\Desktop\\Kcet Predictor\\data\\Colleges.xlsx')
df_colleges["GM"] = pd.to_numeric(df_colleges["GM"], errors="coerce").fillna(99999).astype(int)
df_colleges.fillna("Not Available", inplace=True)

for col in ["college name", "Course Name", "Location", "Type of College", "Websites"]:
    df_colleges[col] = df_colleges[col].astype(str).str.strip()


TOTAL_STUDENTS_PER_YEAR = {2022: 130000, 2023: 244000, 2024: 310000, 2025: 312000, 2026: 318000}

ENGINEERING_BRANCHES = [
    "Any Branch", "Computer Science & Engineering", "ECE", "EEE",
    "Mechanical", "Civil", "AI & ML", "Data Science", "Cyber Security"
]

LOCATIONS = ["Any Location", "Bangalore", "Mysore", "Tumkur", "Belagavi", "Mangalore"]
TYPES = ["Any Type", "VTU", "Auto", "University"]


class Student_Details(BaseModel):
    kcet_marks:int
    board_marks:int
    year_attended:int

class Recommand_Colleges(BaseModel):
    rank:int
    branches:list[str]
    location:str
    college_type:str

@app.post('/predict')
def PredictRank(data: Student_Details):
    cet_marks=data.kcet_marks
    board_marks=data.board_marks
    year=data.year_attended

    cet_marks=(cet_marks/180)*100
    board_marks=(board_marks/300)*100

    score=int((cet_marks/2)+(board_marks/2))

    input=[[score,year,TOTAL_STUDENTS_PER_YEAR[year]]]
    input=scaler.transform(input)

    prank=int(model.predict(input)[0])
    prank+=3000

    return {'estimated_rank':prank}

@app.get('/filters')
def filters():
    return {
        'branch':ENGINEERING_BRANCHES,
        'location':LOCATIONS,
        'type':TYPES
    }

@app.post('/recommandation/')
def recommand_colleges(data:Recommand_Colleges):
    df = df_colleges.copy()
    df = df[df["GM"] >= data.rank]

    if "any branch" not in [b.lower() for b in data.branches]:
        df = df[df["Course Name"].apply(lambda x: matches_branch(x, data.branches))]

    if data.location.lower() != "any location":
        df = df[df["Location"].str.lower().str.contains(data.location.lower())]
    if data.college_type.lower() != "any type":
        df = df[df["Type of College"].str.lower().str.contains(data.college_type.lower())]


    df = df.sort_values("GM", ascending=True)

    return df.to_dict(orient="records")