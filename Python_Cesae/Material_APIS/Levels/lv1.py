# Make the GET request:
# First, let's make the GET request to the API using the requests library, as we did in the previous exercise:

import requests

endpoint = 'https://api.chucknorris.io/jokes/random'

response = requests.get(endpoint)

data = response.json()
print(data)
