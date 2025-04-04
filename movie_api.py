import requests


def fetch_movie_data_from_api(title):
    api_key = '27eb4cc7'  # Dein API-Schlüssel
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