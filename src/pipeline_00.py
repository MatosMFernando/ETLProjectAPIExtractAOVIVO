import requests

def extract_dados_bitcoin():
    # Extrair dados do Bitcoin  
    url = "https://api.coinbase.com/v2/prices/spot"
    response = requests.get(url)
    return response.json()

print(extract_dados_bitcoin())
