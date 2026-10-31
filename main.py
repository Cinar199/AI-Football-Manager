
from fastapi import FastAPI
from teams import ssc_vincia, reale_vincia
from engine.simulation import simulate_match

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
def get_ssc_vincia():
    return {
        "name": ssc_vincia.TEAM_NAME,
        "formation": ssc_vincia.FORMATION,
        "players": [
            {"role": item["role"], **item["player"].info()}
            for item in ssc_vincia.STARTING_XI
        ]
    }


@app.get("/team/reale_vincia")
def get_reale_vincia():
    return {
        "name": reale_vincia.TEAM_NAME,
        "formation": reale_vincia.FORMATION,
        "players": [
            {"role": item["role"], **item["player"].info()}
            for item in reale_vincia.STARTING_XI
        ]
    }


@app.get("/match/test")
def test_match():
    return simulate_match(ssc_vincia, reale_vincia)
    
