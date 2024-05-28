# Process the response and extract the joke:
# After receiving the response from the API, we need to process the data.
# As the API returns the data in JSON format,
# we use the json() method to convert it into a Python object (dictionary).
# We can then access the key containing the Chuck Norris joke and display it:

import requests


endpoint = 'https://api.chucknorris.io/jokes/random'

response = requests.get(endpoint)

data = response.json()

joke = data['value']

print(joke)
