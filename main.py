from fastapi import FastAPI
from teams import ssc_vincia

app = FastAPI(
    title="AI Football Manager",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "project": "AI Football Manager",
        "status": "online"
    }


@app.get("/health")
def health():
    return {
        "online": True,
        "project": "AI Football Manager"
    }


@app.get("/team/ssc_vincia")
def get_team():
    return {
        "name": ssc_vincia.TEAM_NAME,
        "formation": ssc_vincia.FORMATION,
        "players": [
            {
                "role": item["role"],
                **item["player"].info()
            }
            for item in ssc_vincia.STARTING_XI
        ]
    }
