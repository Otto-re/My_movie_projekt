from abc import ABC, abstractmethod

class IStorage(ABC):
    @abstractmethod
    def list_movies(self):
        """Gibt ein Dictionary aller Filme zurück."""
        pass

    @abstractmethod
    def add_movie(self, title, year, rating, poster):
        """Fügt einen neuen Film hinzu."""
        pass

    @abstractmethod
    def delete_movie(self, title):
        """Löscht einen Film."""
        pass

    @abstractmethod
    def update_movie(self, title, rating):
        """Aktualisiert die Bewertung eines bestehenden Films."""
        pass