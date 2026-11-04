import requests

url = "https://official-joke-api.appspot.com/random_joke"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    joke = response.json()

    setup = joke["setup"]
    punchline = joke["punchline"]

    print(setup)
    print(punchline)

    with open("jokes.txt", "w", encoding="utf-8") as file:
        file.write(f"{setup}\n{punchline}\n")

    print("Joke saved to jokes.txt!")

except requests.exceptions.RequestException as error:
    print(f"Could not fetch the joke: {error}")
