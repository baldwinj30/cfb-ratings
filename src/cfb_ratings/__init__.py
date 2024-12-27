import requests
from dotenv import load_dotenv
import os

load_dotenv()


def main() -> None:
    cfbd_api_key = os.getenv("CFBD_API_KEY")
    if cfbd_api_key is None:
        print("Set your api key in a .env file")
        return
    response = requests.get(url="https://api.collegefootballdata.com/games?year=2022", headers={"Authorization": f"Bearer {cfbd_api_key}"})
    print(response.json())
