import os
import requests
from dotenv import load_dotenv

load_dotenv()

DROP_EMAIL = os.getenv("DROPI_EMAIL")
CARTPANDA_TOKEN = os.getenv("CARTPANDA_TOKEN")
CARTPANDA_API_URL = "https://api.cartpanda.com.br/v1/products"

def buscar_produtos_dropi():
    # Simulação: você deve integrar aqui a lógica real de scraping ou API da Dropi
    return [{
        "title": "Cuba Inox Luxo",
        "description": "Cuba moderna para banheiro.",
        "price": 199.99,
        "image": "https://example.com/cuba.jpg"
    }]

def criar_produto_cartpanda(produto):
    headers = {"Authorization": f"Bearer {CARTPANDA_TOKEN}"}
    data = {
        "name": produto["title"],
        "description": produto["description"],
        "price": produto["price"],
        "images": [produto["image"]]
    }
    response = requests.post(CARTPANDA_API_URL, json=data, headers=headers)
    print(f"[{response.status_code}] {response.text}")

def importar_e_enviar():
    produtos = buscar_produtos_dropi()
    for produto in produtos:
        criar_produto_cartpanda(produto)

if __name__ == "__main__":
    importar_e_enviar()