import json
from istorage import IStorage

class StorageJson(IStorage):
    def __init__(self, file_name):
        self._file_name = file_name
        self._load_movies()

    def _load_movies(self):
        try:
            with open(self._file_name, 'r') as file:
                self.movies = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.movies = {}

    def _save_movies(self):
        with open(self._file_name, 'w') as file:
            json.dump(self.movies, file, indent=4)

    def list_movies(self):
        return self.movies

    def add_movie(self, title, year, rating, poster):
        self.movies[title] = {"year": year, "rating": rating, "poster": poster}
        self._save_movies()

    def delete_movie(self, title):
        if title in self.movies:
            del self.movies[title]
            self._save_movies()

    def update_movie(self, title, rating):
        if title in self.movies:
            self.movies[title]["rating"] = rating
            self._save_movies()

    def generate_website(self, template_path="_static/index_template.html", output_path="index.html"):
        try:
            with open(template_path, "r", encoding="utf-8") as file:
                template = file.read()

            movie_grid = ""
            for title, data in self.movies.items():
                movie_grid += f"""
                <div class="movie">
                    <h2>{title}</h2>
                    <p>Year: {data['year']}</p>
                    <p>Rating: {data['rating']}</p>
                    <img src="{data['poster']}" alt="{title} poster">
                </div>
                """

            template = template.replace("__TEMPLATE_TITLE__", "Meine Filmseite")
            template = template.replace("__TEMPLATE_MOVIE_GRID__", movie_grid)

            with open(output_path, "w", encoding="utf-8") as file:
                file.write(template)

            print("Website wurde erfolgreich generiert.")

        except FileNotFoundError:
            print("Fehler: Template-Datei nicht gefunden.")