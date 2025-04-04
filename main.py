from movie_app import MovieApp
from storage_csv import StorageCsv
from storage_json import StorageJson


# Mit CSV arbeiten
storage_csv = StorageCsv('movies.csv')
movie_app_csv = MovieApp(storage_csv)
movie_app_csv.run()

# Mit JSON arbeiten
storage_json = StorageJson('movies.json')
movie_app_json = MovieApp(storage_json)
movie_app_json.run()

if __name__ == "__main__":
    main()