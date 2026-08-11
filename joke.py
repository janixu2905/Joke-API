import requests

url = "https://official-joke-api.appspot.com/random_jokexx"

response = requests.get(url)

try:
    response.raise_for_status()

    data = response.json()

    print("\n😂 Here's your joke:")
    print("\nQ:", data["setup"])
    print("Ans:", data["punchline"])

except requests.exceptions.HTTPError as e:
    print("HTTP ERROR CODE: ",e)
except requests.exceptions.RequestException as e:
    print("Something went wrong: ",e)