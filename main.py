# main.py
from api_calls import get_top_100_cryptos, get_stock_data, get_news_data

def main():
    # Coletando dados das 100 criptomoedas em alta
    print("Coletando dados das 100 criptomoedas em alta...")
    crypto_data = get_top_100_cryptos()
    if crypto_data:
        for crypto in crypto_data:
            print(f"**Criptomoeda**: {crypto['name']} - Preço: ${crypto['current_price']} - Market Cap: ${crypto['market_cap']}")

    # Coletando dados de ações
    print("\nColetando dados de ações em alta...")
    stock_symbols = ["AAPL", "MSFT", "GOOGL", "AMZN", "FB", "NFLX"]  # Exemplo de ações populares
    for symbol in stock_symbols:
        stock_data = get_stock_data(symbol)
        if stock_data:
            # Aqui você pode adicionar lógica para analisar os dados, se necessário
            print(f"Ação: {symbol}, Dados: {stock_data}")

    # Coletando notícias
    print("\nColetando notícias relacionadas a Bitcoin...")
    news_data = get_news_data("bitcoin")
    if news_data:
        print("Dados de Notícias:", news_data)

if __name__ == "__main__":
    main()
