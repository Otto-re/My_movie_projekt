import random
from movie_api import fetch_movie_data_from_api

class MovieApp:
    def __init__(self, storage):
        self._storage = storage

    def _command_list_movies(self):
        movies = self._storage.list_movies()
        if not movies:
            print("No movies available.")
        else:
            for title, info in movies.items():
                print(f"{title} ({info['year']}): {info['rating']}")

    def _command_add_movie(self):
        title = input("Movie title: ")

        movie_data = fetch_movie_data_from_api(title)

        if movie_data:
            print(movie_data)
            year = int(movie_data['year'])
            rating = float(movie_data['rating'])
            poster = movie_data.get('Poster', 'There is no Pic')
            self._storage.add_movie(title, year, rating, poster)
            print(f"Added movie: {title} ({year}), Rating: {rating}, Poster: {poster}")
        else:
            print(f"Movie {title} not found.")

    def _command_delete_movie(self):
        title = input("Enter movie title to delete: ")
        self._storage.delete_movie(title)
        print(f"Deleted movie: {title}")

    def _command_update_movie(self):
        title = input("Enter movie title to update: ")
        if title not in self._storage.list_movies():
            print(f"Movie {title} not found.")
            return
        rating = float(input("Enter new rating: "))
        self._storage.update_movie(title, rating)
        print(f"Updated movie {title}'s rating to {rating}")

    def _command_generate_website(self):
        self._storage.generate_website()

    def _command_stats(self):
        movies = self._storage.list_movies()
        if not movies:
            print("No movies available for statistics.")
            return

        # Durchschnittsbewertung berechnen
        total_rating = sum(movie["rating"] for movie in movies.values())
        average_rating = total_rating / len(movies)
        print(f"Average Rating: {average_rating:.2f}")

    def _command_random_movie(self):
        movies = list(self._storage.list_movies().items())
        if movies:
            random_movie = random.choice(movies)
            print(f"Random Movie: {random_movie[0]} ({random_movie[1]['year']}), Rating: {random_movie[1]['rating']}")
        else:
            print("No movies available.")

    def _command_search_movie(self):
        search_query = input("Enter movie title or part of title to search: ").lower()
        movies = self._storage.list_movies()
        found_movies = {title: data for title, data in movies.items() if search_query in title.lower()}
        if found_movies:
            for title, data in found_movies.items():
                print(f"{title} ({data['year']}), Rating: {data['rating']}")
        else:
            print(f"No movies found matching '{search_query}'.")

    def _command_sorted_by_rating(self):
        movies = self._storage.list_movies()
        if not movies:
            print("No movies available to sort.")
            return
        sorted_movies = sorted(movies.items(), key=lambda x: x[1]["rating"], reverse=True)
        for title, data in sorted_movies:
            print(f"{title} ({data['year']}), Rating: {data['rating']}")

    def run(self):
        while True:
            print("\nMenu:")
            print("0. Exit")
            print("1. List Movies")
            print("2. Add Movie")
            print("3. Delete Movie")
            print("4. Update Movie")
            print("5. Stats")
            print("6. Random Movie")
            print("7. Search Movie")
            print("8. Movies Sorted by Rating")
            print("9. Generate Website")
            choice = input("Enter choice (0-9): ")

            if choice == "0":
                break
            elif choice == "1":
                self._command_list_movies()
            elif choice == "2":
                self._command_add_movie()
            elif choice == "3":
                self._command_delete_movie()
            elif choice == "4":
                self._command_update_movie()
            elif choice == "5":
                self._command_stats()
            elif choice == "6":
                self._command_random_movie()
            elif choice == "7":
                self._command_search_movie()
            elif choice == "8":
                self._command_sorted_by_rating()
            elif choice == "9":
                self._command_generate_website()
            else:
                print("Invalid choice.")