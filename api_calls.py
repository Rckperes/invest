# api_calls.py
import requests

# Sua chave de API da NewsAPI
NEWS_API_KEY = "3b4cc81b93634b80a92c576d719771d8"

def get_top_100_cryptos():
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro ao obter dados de criptomoedas: {response.status_code}")
        return None

def get_stock_data(symbol):
    alpha_vantage_api_key = "4F0INQ7OCBWM661J"  # Substitua com a sua chave
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={alpha_vantage_api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro ao obter dados de ações: {response.status_code}")
        return None

def get_news_data(keyword):
    url = f"https://newsapi.org/v2/everything?q={keyword}&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro ao obter dados de notícias: {response.status_code} - {response.text}")
        return None
