import requests
import pandas as pd
import sqlalchemy as sa
import sqlite3 as sql
from config import API_KEY, API_CONFIG

def get_Alpha_Vantage(symbol, parameters, API_KEY):
    ALPHA_KEY = API_KEY["ALPHA_KEY"]
    ALPHA_CONFIG = API_CONFIG["ALPHA_CONFIG"]
    ALPHA_FUNCTIONS_MAP = {
        "1": "TIME_SERIES_INTRADAY",
        "2": "TIME_SERIES_DAILY",
        "3": "TIME_SERIES_WEEKLY",
        "4": "TIME_SERIES_MONTHLY"
    }

    try:
        response = requests.get(Base_URL, params = parameters)
        response.raise_for_status()
        return response.json()

    except Exception as e:
        print("Error", e)
        return None