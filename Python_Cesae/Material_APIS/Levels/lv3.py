# Dealing with errors and exceptions.
# In this exercise, we'll add error handling to our code to deal with
# possible connection problems with the API or errors in the response.

import requests


endpoint = "https://api.chucknorris.io/jokes/random"


def fetchAPI(url):
    try:
        response = requests.get(url)
        data = response.json()
        joke = data["value"]
        print("Joke:", joke)

    except:
        print("Something is wrong!")


fetchAPI(endpoint)
