Quantitative Trading Data Pull

This project fetches real-time and historical stock and cryptocurrency data from multiple sources and organizes it into tables and charts for easy analysis. It helps me practice Python, APIs, and data visualization while learning about financial markets.

Features
- Fetches stock prices from multiple sources
- Organizes data into easy-to-read tables and charts
- Uses caching to speed up searches
- Avoids sending too many requests with rate limiting
- Simple graphical interface for searching stocks

How to Install and Run

1. Download the Project
   git clone https://github.com/aye-ko/QuantTradingProject
   cd QuantTradingProject

2. Set Up a Virtual Environment
   python -m venv env

   - Mac/Linux: source env/bin/activate  
   - Windows: env\Scripts\activate  

3. Install Required Packages
   pip install -r requirements.txt

How It Works

1. Enter a stock symbol (e.g., AAPL)
2. The program checks memory to see if data is already available
3. If needed, it fetches data from stock websites
4. Data is organized and displayed in a graph

Run the App

   python main.py

A window will open where you can:
- Enter a stock name
- Choose data sources
- Click Fetch Data to view real-time prices

Security
- API keys are stored in a .env file
- Missing keys will show a warning

License
This project is open-source under the MIT License.
