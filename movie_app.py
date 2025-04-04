from movie_api import fetch_movie_data_from_api


class MovieApp:
    def __init__(self, storage):
        self._storage = storage

    def _command_list_movies(self):
        movies = self._storage.list_movies()
        for title, info in movies.items():
            print(f"{title} ({info['year']}): {info['rating']}")

    def _command_add_movie(self):
        title = input("Movie title: ")

        movie_data = fetch_movie_data_from_api(title)

        if movie_data:
            # Wenn Daten gefunden wurden, füge sie hinzu
            year = int(movie_data['year'])
            rating = float(movie_data['rating'])
            poster = movie_data['Poster']
            self._storage.add_movie(title, year, rating, poster)
            print(f"Added movie: {title} ({year}), Rating: {rating}")
        else:
            print(f"Movie {title} not found.")

    def _command_delete_movie(self):
        title = input("Enter movie title to delete: ")
        self._storage.delete_movie(title)

    def _command_update_movie(self):
        title = input("Enter movie title to update: ")

        # Überprüfen, ob der Film existiert, bevor der Rating-Wert geändert wird
        if title not in self._storage.list_movies():
            print(f"Movie {title} not found.")
            return

        rating = float(input("Enter new rating: "))
        self._storage.update_movie(title, rating)

    def _command_generate_website(self):
        self._storage.generate_website()

    def run(self):
        while True:
            print("\nMenu:")
            print("1. List Movies")
            print("2. Add Movie")
            print("3. Delete Movie")
            print("4. Update Movie")
            print("5. Generate website")
            print("6. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                self._command_list_movies()
            elif choice == "2":
                self._command_add_movie()
            elif choice == "3":
                self._command_delete_movie()
            elif choice == "4":
                self._command_update_movie()
            elif choice == "5":
                self._command_generate_website()
            elif choice == "6":
                break
            else:
                print("Invalid choice.")