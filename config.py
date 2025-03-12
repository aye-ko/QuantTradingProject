import os
from dotenv import load_dotenv
# Load the API key and print out which one were loaded and which failed

load_dotenv()

missing_key = [] # to store failed keys 
try:
# DIctionary to to pull the api keys and save it to theh respective api
    API_KEY = {
        "ALPHA_KEY"      :os.getenv("ALPHA_KEY"),
        "FINNHUB_KEY"    :os.getenv("FINNHUB_KEY"),
        "TIINGO_KEY"     :os.getenv("TIINGO_KEY"),
        "POLYGON_KEY"    :os.getenv("POLYGON_KEY"),
        "ALPACA_KEY"     :os.getenv("ALPACA_KEY"),
        "ALPACA_SEC_KEY" :os.getenv("ALPACA_SEC_KEY")
    }

    # for look to loop through and sort which ones have been assigned and which failed 
    for key_name, key_value in API_KEY.items():
        if key_value is None:
            missing_key.append(key_name) #failed apis loading is appened here

    if len(missing_key) > 0:
        print(f"Missing API Key(s): {','.join(missing_key)}") #print out missing key if any
    else:
        print("I have the keys.")

        # This is a dictionary to assign the right names and tokens to the correct API
    API_CONFIG = {
        "ALPHA_CONFIG"   : {
            "Base_URL"    : "https://www.alphavantage.co/query",
            "parameters"  : {
                "symbol"  :"symbol",
                "API_KEY" : "apikey"
            } 
        },

        "ALPACA_CONFIG" : {
            "Base_URL"     : "https://paper-api.alpaca.markets/v2/stocks",
            "parameters"   : {
                "symbol"   : "symbol",
                "timeframe": {"1Day","1Min","5Min", "15Min", "1Hour"}
            }
        },

        "FINNHUB_CONFIG" : {
            "Base_URL" : "https://finnhub.io/api/v1",
            "parameters" : {
                "symbol" : "symbol",
                "API_KEY": "token"
            }
        },

        "POLYGON_CONFIG" : {
            "Base_URL" : "https:api.polygon.io/v2",
            "parameters" : {
                "symbol" : "ticker",
                "API_KEY" : "apiKey"
            }
        },

        "TIINGO_CONFIG" : {
            "Base_URL" : "https://api.tiingo.com",
            "parameters" : {
                "symbol" : "ticker",
                "API_KEY" : "token"
            }
        }
    }
except Exception as e:
    print("An error occured:", e)