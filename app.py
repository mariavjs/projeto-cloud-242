import requests

# Base URL pública do endpoint (ajuste conforme necessário)
BASE_URL = "http://a2106d20f94614475ac81799589167c3-2084239673.us-west-2.elb.amazonaws.com"

# Dados para registro e login
user_data = {
    "name": "Test User",
    "email": "testeee@example.com",
    "password": "password123"
}

def test_register():
    """Testa o endpoint de registro."""
    print("\nTesting /register endpoint...")
    url = f"{BASE_URL}/registrar"
    response = requests.post(url, json=user_data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

def test_login():
    """Testa o endpoint de login."""
    print("\nTesting /login endpoint...")
    url = f"{BASE_URL}/login"
    login_data = {
        "email": user_data["email"],
        "password": user_data["password"]
    }
    response = requests.post(url, json=login_data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
    return response.json().get("jwt")

def test_consultar(jwt_token):
    """Testa o endpoint de consulta."""
    print("\nTesting /consultar endpoint...")
    url = f"{BASE_URL}/consultar"
    headers = {"Authorization": f"Bearer {jwt_token}"}
    response = requests.get(url, headers=headers)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

if __name__ == "__main__":
    print("Testing API Endpoints...")
    
    # Testa o registro
    test_register()
    
    # Testa o login e obtém o token JWT
    jwt_token = test_login()
    
    if jwt_token:
        # Testa o endpoint protegido com o token JWT
        test_consultar(jwt_token)
    else:
        print("Login falhou. Não foi possível testar o endpoint de consulta.")
