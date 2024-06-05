import requests
import json

endpoint = "https://pokeapi.co/api/v2/pokemon/"
pokemonList = list()

counter = 1

# Pagination
while endpoint != None:
    payload = {}
    headers = {}
    response = json.loads(requests.request(
        "GET", endpoint, headers=headers, data=payload).text)

    # Pagination Url
    endpoint = response["next"]

    allPokemons = response["results"]

    for pokemon in allPokemons:
        pokemonName = pokemon['name']
        endpointPokemon = f"https://pokeapi.co/api/v2/pokemon/{pokemonName}"
        responsePokemon = json.loads(requests.request(
            "GET", endpointPokemon, headers=headers, data=payload).text)

        # Catch this data to Each Pokemon
        info = {
            "name": pokemonName,
            "id": responsePokemon["id"],
            "height": responsePokemon["height"],
            "weight": responsePokemon["weight"],
            "is_default": responsePokemon["is_default"],
        }

        pokemonList.append(info)
        print(responsePokemon["id"])

        # Path to save file
        filePath = fr"APIs_Use\Pokemon\json\pokemonFile{counter}.json"

    # Save File
    with open(filePath, "w") as outfile:
        print(f"Saving File in: {filePath}")
        # Doing Dump(what to save, who save)
        json.dump(pokemonList, outfile)
    outfile.close()
    counter = counter + 1

    # Clear List
    pokemonList = list()


print(pokemonList)
