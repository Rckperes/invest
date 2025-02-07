import streamlit as st
from api_calls import get_top_100_cryptos, get_news_data

def main():
    st.title("Dados de Criptomoedas e Ações")

    # Coletar dados das 100 criptomoedas
    st.header("Top 100 Criptomoedas")

    # Obter os dados de criptomoedas
    crypto_data = get_top_100_cryptos()
    
    # Barra de pesquisa para filtrar criptomoedas
    search_term = st.text_input("Pesquise uma criptomoeda:")

    if crypto_data:
        # Filtrar criptomoedas com base na pesquisa
        if search_term:
            filtered_crypto_data = [crypto for crypto in crypto_data if search_term.lower() in crypto['name'].lower()]
        else:
            filtered_crypto_data = crypto_data
        
        # Compactar em uma seção
        with st.expander("Clique para ver as 100 Criptomoedas", expanded=True):
            for crypto in filtered_crypto_data:
                st.write(f"**Criptomoeda**: {crypto['name']}")
                st.write(f"**Preço em Tempo Real**: ${crypto['current_price']}")
                st.write(f"[Acompanhe em tempo real]({crypto['id']})")  # Use o ID ou outra URL para acompanhar
                st.write("---")  # Separador

    # Coletando notícias
    st.header("Notícias sobre Bitcoin")
    news_data = get_news_data("bitcoin")
    if news_data and 'articles' in news_data:
        for article in news_data['articles']:
            st.subheader(article['title'])
            st.write(f"**Fonte**: {article['source']['name']}")
            st.write(f"**Autor**: {article['author'] if article['author'] else 'Desconhecido'}")
            st.write(f"**Data de Publicação**: {article['publishedAt']}")
            st.write(f"**Descrição**: {article['description']}")
            st.write(f"[Leia mais]({article['url']})")
            st.write(f"**Imagem**: ![]({article['urlToImage']})")
            st.write("---")  # Separador

if __name__ == "__main__":
    main()
