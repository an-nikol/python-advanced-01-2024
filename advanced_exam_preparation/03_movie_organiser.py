def movie_organizer(*args):
    genre_movies = {}

    for movie, genre in args:
        if genre not in genre_movies:
            genre_movies[genre] = []
        genre_movies[genre].append(movie)

    genre_movies = dict(sorted(genre_movies.items(), key=lambda x: (-len(x[1]), x[0])))

    result = ''

    for genre, movies in genre_movies.items():
        result += f"\n{genre} - {len(movies)}\n* "
        result += '\n* '.join(sorted(movies))
    return result

print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))
