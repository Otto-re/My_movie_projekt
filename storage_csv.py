from fileinput import filename

import csv
from istorage import IStorage

class StorageCsv(IStorage):
    def __init__(self, file_name):
        self._file_name = file_name
        self.movies = self._load_movies()

    def _load_movies(self):
        """
        lädt die filme aus der csv datei in ein dictionary
        """
        movies = {}
        try:
            with open(self._file_name, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    movies[row["titel"]] = {
                        "year": int (row["year"]),
                        "rating": float(row["rating"]),
                        "poster": row ["poster"]
                    }
        except FileNotFoundError:
            pass
        return movies

    def _save_movies(self):
        """
        Speichert das Dictionary mit den Filmen in der CSV-Datei.
        """
        with open(self._file_name, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ["title", "year", "rating", "poster"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for title, data in self.movies.items():
                writer.writerow(
                    {"title": title, "year": data["year"], "rating": data["rating"], "poster": data["poster"]}
                )

    def list_movies(self):
        """
                Speichert das Dictionary mit den Filmen in der CSV-Datei.
                """
        with open(self._file_name, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ["title", "year", "rating", "poster"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for title, data in self.movies.items():
                writer.writerow(
                    {"title": title, "year": data["year"], "rating": data["rating"], "poster": data["poster"]}
                )

    def list_movies(self):
        """
        Gibt das Dictionary aller Filme zurück.
        """
        return self.movies

    def add_movie(self, title, year, rating, poster):
        """
        Fügt einen neuen Film hinzu und speichert ihn in der CSV-Datei.
        """
        self.movies[title] = {"year": year, "rating": rating, "poster": poster}
        self._save_movies()

    def delete_movie(self, title):
        """
        Löscht einen Film anhand des Titels und speichert die Änderung.
        """
        if title in self.movies:
            del self.movies[title]
            self._save_movies()

    def update_movie(self, title, rating):
        """
        Aktualisiert die Bewertung eines Films und speichert die Änderung.
        """
        if title in self.movies:
            self.movies[title]["rating"] = rating
            self._save_movies()
