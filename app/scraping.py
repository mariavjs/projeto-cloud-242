import requests
import random
from fastapi.responses import StreamingResponse
from io import BytesIO

def get_random_dog():
    # Gera um código HTTP aleatório entre 100 e 599
    
    url = "https://www.world-wonders-api.org/v0/wonders/random"

    
    try:
        # Fazer a requisição para obter a imagem
        response = requests.get(url)
        
        response.raise_for_status()  # Verifica se houve erro na requisição
        fato = response.json()["summary"]
        # Retorna a imagem como resposta de streaming
        return {"fato": fato}
        
    except requests.RequestException as e:  
        # Retorna um erro 500 em caso de erro na requisição
        return {"erro" : "Erro ao obter a api"}
    
print(get_random_dog())