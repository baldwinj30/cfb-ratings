"""Experimental script."""

import os

import polars as pl
import requests
from dotenv import load_dotenv

load_dotenv()


def main() -> None:
    """Test functionality."""
    cfbd_api_key = os.getenv("CFBD_API_KEY")
    if cfbd_api_key is None:
        print("Set your api key in a .env file")
        return
    response = requests.get(
        url="https://api.collegefootballdata.com/games?year=2014",
        headers={"Authorization": f"Bearer {cfbd_api_key}"},
    )
    df = pl.from_dicts(
        response.json(),
        schema={
            "id": pl.Int64,
            "season": pl.Int64,
            "week": pl.Int64,
            "home_id": pl.Int64,
            "home_team": pl.String,
            "home_conference": pl.String,
            "home_division": pl.String,
            "home_points": pl.Int64,
            "away_id": pl.Int64,
            "away_team": pl.String,
            "away_conference": pl.String,
            "away_division": pl.String,
            "away_points": pl.Int64,
        },
    )
    print(df)
