import requests

# endpoint
endpoint = 'https://jsonplaceholder.typicode.com/posts'

# request by get
response = requests.get(endpoint)

# check
try:
    response.status_code == 200
    data = response.json()
    print(data)
except:
    print("Something is wrong!")
