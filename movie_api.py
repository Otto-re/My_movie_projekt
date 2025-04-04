import requests
from dotenv import load_dotenv
import os

load_dotenv()

def fetch_movie_data_from_api(title):
    api_key = os.getenv("OMDB_API_KEY")  # Dein API-Schlüssel
    if not api_key:
        print("API key not found!")
        return None
    url = f"http://www.omdbapi.com/?t={title}&apikey={api_key}"

    try:

        response = requests.get(url)
        response.raise_for_status()

        if response.status_code == 200:
            movie_data = response.json()
            if movie_data['Response'] == 'True':
                return {
                    'title': movie_data['Title'],
                    'year': movie_data['Year'],
                    'rating': movie_data['imdbRating'],
                    'poster': movie_data['Poster'],
                }
            else:
                print(f"Movie not found: {title}")
                return None
        else:
            print("Failed to fetch data")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Failed to converse with API: {e}")
        return None