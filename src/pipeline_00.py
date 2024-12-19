import requests

def extract_dados_bitcoin():
    # Extrair dados do Bitcoin  
    url = "https://api.coinbase.com/v2/prices/spot"
    response = requests.get(url)
    return response.json()

def transform_dados_bitcoin(dados):
    valor = dados['data']['amount']
    currency = dados['data']['base']
    moeda = dados['data']['currency']

    dados_transformados = {
        'valor': valor,
        'currency': currency,
        'moeda': moeda
    }

    return dados_transformados

if __name__ == "__main__":
    dados_json = extract_dados_bitcoin()
    dados_transformados = transform_dados_bitcoin(dados_json)
    print(dados_transformados)

