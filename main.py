from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl
from fastapi.responses import JSONResponse
import datetime

app = FastAPI()


def current_day():
  return datetime.date.today()


def get_utc_time():
    current_utc_time = datetime.datetime.utcnow()
    time_plus_2_minutes = current_utc_time + datetime.timedelta(minutes=2)
    time_minus_2_minutes = current_utc_time - datetime.timedelta(minutes=2)
    current_time = datetime.datetime.utcnow()

    if time_minus_2_minutes <= current_time <= time_plus_2_minutes:
        return current_time.strftime("%Y-%m-%dT%H:%M:%SZ")
  
  
entries = [{
  "slack_name": "HNGx",
  "current_day": current_day().strftime("%A"),
  "utc_time": get_utc_time(),
  "track": "backend",
  "github_file_url": "https://github.com/Timmy-Edibo/HNGx_Backend/blob/stage_one/main.py",
  "github_repo_url": "https://github.com/Timmy-Edibo/HNGx_Backend",
  "status_code": 200
}]
  
@app.get("/api")
def profile(slack_name: str, track: str):
  for entry in entries:
    return JSONResponse(entry) if (
      entry["slack_name"].lower() == slack_name.lower() and entry["track"].lower() == track.lower()
      ) else JSONResponse([])

