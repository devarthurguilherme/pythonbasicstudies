import requests

# endpoint
endpoint = 'https://jsonplaceholder.typicode.com/posts'

# request by get
# Essa linha faz uma requisição GET para a URL especificada utilizando a biblioteca requests do Python.
# O resultado da requisição é armazenado na variável response.
response = requests.get(endpoint)

# check
try:
    # Essa linha verifica se o código de status da resposta da requisição é igual a 200,
    # o que indica que a requisição foi bem-sucedida.
    response.status_code == 200


# converte o conteúdo da resposta da requisição, que está em formato JSON, para um objeto Python.
# Esse objeto é então armazenado na variável data para ser utilizado posteriormente no código.
    data = response.json()
    print(data)
except:
    print("Something is wrong!")
