import requests

def fetch_random_dog_image():
    url = "https://dog.ceo/api/breeds/image/random"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data["status"] == "success":
            print(f"Voici une image aléatoire d'un chien : {data['message']}")
        else:
            print("Erreur lors de la récupération de l'image.")
    except requests.RequestException as e:
        print(f"Une erreur est survenue : {e}")

if __name__ == "__main__":
    fetch_random_dog_image()
