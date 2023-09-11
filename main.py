from fastapi import FastAPI
from datetime import datetime
import pytz

app = FastAPI()

@app.get("/")
def home(slack_name:str = "Pamode", track:str = "backend"):
    now = datetime.now(pytz.UTC)
    utc_time = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    current_day = now.strftime("%A")
    return {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": "https://github.com/Pamode-Ukwe/Hng-Backend-Stage-1/blob/master/main.py",
        "github_repo_url": "https://github.com/Pamode-Ukwe/Hng-Backend-Stage-1",
        "status_code": 200
    }
