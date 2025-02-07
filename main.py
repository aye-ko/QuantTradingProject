try: 
    import os
    from dotenv import load_dotenv
    import requests
    import pandas as pd

except ModuleNotFoundError as e:
    print(f"Missing Library: {e.name}")
    print(f"Try instaling it with: 'pip install " + e.name + "'") #install the missing module
    exit(1) #exit the whole program so that the user can install the required modules


class DataPull:


    def __init__(self):
        self.API_Keys = self.loadAPI_Keys()
        self.apiMappings = self.initialize_apiMappings()


    def loadAPI_Keys(self):

        try: 
            load_dotenv()
            API_Keys = {
                 
                "ALPHA_KEY" : os.getenv("ALPHA_KEY"),
                "FINNHUB_KEY" : os.getenv("FINNHUB_KEY"),
                "POLYGON_KEY" : os.getenv("POLYGON_KEY"),
                "TIINGO_KEY" : os.getenv("TIINGO_KEY")
            }

            missing_keys = [key for key, value in API_Keys.items() if value is None]

            if missing_keys:
                print(f"Warning: Missing API Keys: {','.join(missing_keys)}")
                print("Ensure your .env file is properly configured.")

            for key, value in API_Keys.items():
                if value is None:
                    raise ValueError(f"Missing {key}. Ensure it is correctly set in the .env file.")
                
                return API_Keys
            
        except ValueError as e:
            print(f"ERROR: {str(e)} is invalid or missing. Check .env file and try again")
            exit(1)


    def initialize_apiMappings(self):
            
            return {
                
                "alpha_vantage": {
                    "base_url": "https://www.alphavantage.co/query",
                    "param_name": "symbol",
                    "api_key": self.API_Keys[ALPHA_KEY],
                    "functions": {  # Stores all available functions
                        "daily": "TIME_SERIES_DAILY",
                        "intraday": "TIME_SERIES_INTRADAY",
                        "weekly": "TIME_SERIES_WEEKLY",
                        "monthly": "TIME_SERIES_MONTHLY",
                        "crypto_daily": "DIGITAL_CURRENCY_DAILY",
                        "crypto_intraday": "CRYPTO_INTRADAY",
                        "forex": "CURRENCY_EXCHANGE_RATE",
                        "macd": "MACD",
                        "rsi": "RSI",
                        "sma": "SMA",
                        "ema": "EMA",
                    }
                },

                "finnhub": {
                    "base_url": "https://finnhub.io/api/v1/quote",
                    "param_name": "symbol",
                    "api_key": self.API_Keys[FINNHUB_KEY],
                },

                "polygon": {
                    "base_url": "https://api.polygon.io/v1/open-close",
                    "param_name": "ticker",
                    "api_key": self.API_Keys[POLYGON_KEY],
                },
                "tiingo": {
                    "base_url": "https://api.tiingo.com/tiingo/daily",
                    "param_name": "ticker",
                    "api_key": self.API_Keys[TIINGO_KEY],
                }
            }

    def getAPIwithCorrectParam(self, api_name,symbol):

        if api_name in self.apiMappings:
            param_name = self.apiMappings[api_name]["param_name"]
            return {param_name: symbol}
        
        else:
            raise ValueError(f"Unknown API: {api_name}")
        
    def fetch_data(self, api_name, symbol):
        "Fetch stock data from the selected API"
        try:
            if api_name not in self.apiMappings:
                raise ValueError(f"Unknown API: {api_name}")
            
            api_config = self.apiMappings[api_name]
            params = self.getAPIwithCorrectparam(api_name,symbol)
            params["apikey"] = api_config["api_key"]
            response = requests.get(api_config["base_url"], params = params)

            if response.status_code == 200:
                return response.json()
            else:
                return f"Error: {response.status_code} - {response.text}"
            

        except Exception as e:
            return f"Error fetching data: {str(e)}"



def main():
    if __name__ == "__main__":
        dp = DataPull()  # Create an instance of DataPull class
        symbol = input("Enter a stock ticker (e.g., AAPL, TSLA): ").strip().upper()

        api_choice = input("Choose an API (alpha_vantage, finnhub, polygon, tiingo): ").strip().lower()

        try:
            data = dp.fetch_data(api_choice, symbol)
            print("📊 Stock Data:", data)
        except ValueError as e:
            print(f"❌ Error: {str(e)}")


main()