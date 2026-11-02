
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from teams import (
    ssc_vincia,
    reale_vincia,
    ermis_sc,
    ss_carthage,
    juventus,
    as_roma,
    fk_zeyzella,
    acf_fiorentina,
    ss_lazio,
    us_torino,
    genoa_cfc,
    hajduk_split,
    fc_basel,
    sk_sturm_graz,
    rb_salzburg,
    inter,
    ac_milan,
    reale_monaco
)

from engine.simulation import simulate_match


app = FastAPI(
    title="AI Football Manager",
    version="1.8.0"
)


TEAMS = {
    "ssc_vincia": ssc_vincia,
    "reale_vincia": reale_vincia,
    "ermis_sc": ermis_sc,
    "ss_carthage": ss_carthage,
    "juventus": juventus,
    "as_roma": as_roma,
    "fk_zeyzella": fk_zeyzella,
    "acf_fiorentina": acf_fiorentina,
    "ss_lazio": ss_lazio,
    "us_torino": us_torino,
    "genoa_cfc": genoa_cfc,
    "hajduk_split": hajduk_split,
    "fc_basel": fc_basel,
    "sk_sturm_graz": sk_sturm_graz,
    "rb_salzburg": rb_salzburg,
    "inter": inter,
    "ac_milan": ac_milan,
    "reale_monaco": reale_monaco
}


# Şampiyonluk oranları (%)
CHAMPIONSHIP_ODDS = {
    "inter": 18.0,
    "juventus": 16.0,
    "ac_milan": 12.0,
    "ssc_vincia": 12.0,
    "reale_vincia": 8.0,
    "ermis_sc": 6.0,
    "fk_zeyzella": 6.0,
    "as_roma": 6.0,
    "acf_fiorentina": 6.0,
    "ss_lazio": 3.0,
    "us_torino": 2.0,

    "ss_carthage": 5 / 7,
    "genoa_cfc": 5 / 7,
    "hajduk_split": 5 / 7,
    "fc_basel": 5 / 7,
    "sk_sturm_graz": 5 / 7,
    "rb_salzburg": 5 / 7,
    "reale_monaco": 5 / 7
}


class MatchRequest(BaseModel):
    home: str
    away: str

    home_tactic: str = "dengeli"
    away_tactic: str = "dengeli"

    home_instruction: str = Field(
        default="",
        max_length=2000
    )

    away_instruction: str = Field(
        default="",
        max_length=2000
    )


def calculate_title_bonus(team_id):
    odds = CHAMPIONSHIP_ODDS.get(team_id, 0)
    return round(odds * 0.15, 3)


def format_events(events):
    lines = []

    for event in events:
        minute = event["minute"]

        team = event["team"]

        player = event.get("player") or event.get(
            "scorer",
            "Bilinmiyor"
        )

        event_type = event["type"]

        if event_type == "goal":
            assist = event.get("assist")

            line = f"⚽ {minute}' {player}"

            if assist:
                line += f" (Asist: {assist})"

        elif event_type == "yellow_card":
            line = f"🟨 {minute}' {player} - Sarı kart"

        elif event_type == "red_card":
            line = f"🟥 {minute}' {player} - Kırmızı kart"

        elif event_type == "second_yellow":
            line = f"🟨 {minute}' {player} - İkinci sarı kart"

        elif event_type == "injury":
            line = f"🚑 {minute}' {player} - Sakatlık"

        else:
            # Oyuncu değişiklikleri dahil diğer olaylar gösterilmez.
            continue

        lines.append(f"**{line}** — {team}")

    return "\n".join(lines) if lines else (
        "Maçta kayda değer olay yaşanmadı."
    )


def validate_teams(home, away):
    if home not in TEAMS or away not in TEAMS:
        raise HTTPException(
            status_code=404,
            detail="Takım bulunamadı."
        )

    if home == away:
        raise HTTPException(
            status_code=400,
            detail="Takım kendisiyle oynayamaz."
        )


def prepare_match_result(result):
    result["formatted_events"] = format_events(
        result.get("events", [])
    )

    return result


def run_match(
    home_id,
    away_id,
    home_tactic="dengeli",
    away_tactic="dengeli",
    home_instruction="",
    away_instruction=""
):
    home_title = calculate_title_bonus(home_id)
    away_title = calculate_title_bonus(away_id)

    result = simulate_match(
        TEAMS[home_id],
        TEAMS[away_id],

        home_tactic=home_tactic,
        away_tactic=away_tactic,

        home_instruction=home_instruction,
        away_instruction=away_instruction,

        home_title_bonus=home_title,
        away_title_bonus=away_title
    )

    result["home_id"] = home_id
    result["away_id"] = away_id

    result["home_championship_odds"] = CHAMPIONSHIP_ODDS[home_id]
    result["away_championship_odds"] = CHAMPIONSHIP_ODDS[away_id]

    result["home_title_bonus"] = home_title
    result["away_title_bonus"] = away_title

    return prepare_match_result(result)


@app.get("/")
def home():
    return {
        "project": "AI Football Manager",
        "version": "1.8.0",
        "status": "online"
    }


@app.get("/health")
def health():
    return {
        "online": True,
        "project": "AI Football Manager",
        "version": "1.8.0"
    }


@app.get("/teams")
def get_teams():
    return {
        "teams": [
            {
                "id": team_id,
                "name": team.TEAM_NAME,
                "formation": team.FORMATION,
                "championship_odds": CHAMPIONSHIP_ODDS[team_id],
                "title_bonus": calculate_title_bonus(team_id)
            }
            for team_id, team in TEAMS.items()
        ]
    }


@app.get("/team/{team_id}")
def get_team(team_id: str):
    if team_id not in TEAMS:
        raise HTTPException(
            status_code=404,
            detail="Takım bulunamadı."
        )

    team = TEAMS[team_id]

    return {
        "id": team_id,
        "name": team.TEAM_NAME,
        "formation": team.FORMATION,

        "players": [
            {
                "role": item["role"],
                **item["player"].info()
            }
            for item in team.STARTING_XI
        ]
    }


@app.get("/championship-odds")
def get_championship_odds():
    return {
        "teams": [
            {
                "id": team_id,
                "name": TEAMS[team_id].TEAM_NAME,
                "odds": CHAMPIONSHIP_ODDS[team_id],
                "bonus": calculate_title_bonus(team_id)
            }
            for team_id in TEAMS
        ],

        "total": round(
            sum(CHAMPIONSHIP_ODDS.values()),
            3
        )
    }


@app.get("/match")
def play_match(
    home: str = "ssc_vincia",
    away: str = "reale_vincia"
):
    validate_teams(home, away)

    return run_match(home, away)


@app.post("/match")
def play_custom_match(data: MatchRequest):
    validate_teams(
        data.home,
        data.away
    )

    if data.home_tactic.lower() not in [
        "defansif",
        "dengeli",
        "ofansif"
    ]:
        raise HTTPException(
            status_code=400,
            detail="Geçersiz ev sahibi taktiği."
        )

    if data.away_tactic.lower() not in [
        "defansif",
        "dengeli",
        "ofansif"
    ]:
        raise HTTPException(
            status_code=400,
            detail="Geçersiz deplasman taktiği."
        )

    return run_match(
        data.home,
        data.away,

        home_tactic=data.home_tactic,
        away_tactic=data.away_tactic,

        home_instruction=data.home_instruction,
        away_instruction=data.away_instruction
)
    
