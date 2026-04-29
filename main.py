import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("MY_API_KEY")
if not API_KEY:
    raise ValueError("API key not found. Did you copy .env.example to .env?")

# Using NASA's webiste to gain information
BASE_URL = "https://api.nasa.gov"


def divider(label):
    print(f"\n{'=' * 50}\n{label}\n{'=' * 50}")


# ── Call 1: APOD ───────────────────────────────
# Retrieves the Astronomy Picture of the Day (title, date, explanation) from NASA's APOD AI
def call_one_get():
    divider("CALL 1 — APOD (Astronomy Picture of the Day)")

    url = f"{BASE_URL}/planetary/apod"
    params = {"api_key": API_KEY}  # TODO: update these

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        print("Title:", data["title"])
        print("Date:", data["date"])
        print("Explanation:", data["explanation"][:200], "...")
    else:
        print(f"[ERROR] {response.status_code}: {response.text}")


# ── Call 2: EPIC Earth Data ───────────────────
# Retrieves satellite image metadata from NASA's EPIC API
def call_two_get():
    divider("CALL 2 — EPIC Earth Image Data")

    url = f"{BASE_URL}/EPIC/api/natural"
    params = {
        "api_key": API_KEY
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()

        if data:
            print("Image Identifier:", data[0]["identifier"])
            print("Caption:", data[0]["caption"])
            print("Date:", data[0]["date"])
        else:
            print("No EPIC image data found.")
    else:
        print(f"[ERROR] {response.status_code}: {response.text}")


# ── Call 3: Asteroid Data ─────────────────────
# Call NASA NEO API to get the number of near-earth objects for a specific date
def call_three_parameterized(user_input: str):
    divider(f"CALL 3 — Asteroids for {user_input}")

    url = f"{BASE_URL}/neo/rest/v1/feed"
    params = {
        "api_key": API_KEY,
        "start_date": user_input,
        "end_date": user_input
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        count = data["element_count"]
        print("Number of asteroids:", count)
    else:
        print(f"[ERROR] {response.status_code}: {response.text}")


if __name__ == "__main__":
    call_one_get()
    call_two_get()
    call_three_parameterized("2004-11-09")
