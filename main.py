from fastapi import FastAPI, HTTPException
import pandas as pd

app = FastAPI(title="Unemployment API", version="1.0")

# Load dataset once at startup
df = pd.read_csv("data/unemployment.csv")

@app.get("/")
def home():
    return {"message": "Unemployment Data API - EU5 countries"}

@app.get("/api/countries")
def get_countries():
    countries = df["Country"].unique().tolist()
    return {"countries": countries}

@app.get("/api/unemployment")
def get_unemployment(country: str):
    country = country.capitalize()
    if country not in df["Country"].values:
        raise HTTPException(status_code=404, detail="Country not found")

    data = df[df["Country"] == country][["Year", "Rate"]].to_dict(orient="records")
    return {"country": country, "data": data}
