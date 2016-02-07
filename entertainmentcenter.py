import MovieWeb
import fresh_tomatoes

#Each variable is creating an instance to be collated in the list 'movies'

toy_story = MovieWeb.Movie("Toy Story",
                        "A story of a boy and his toys that come from West Philidelphia",
                        "http://ia.media-imdb.com/images/M/MV5BMTgwMjI4MzU5N15BMl5BanBnXkFtZTcwMTMyNTk3OA@@._V1__SX1303_SY547_.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = MovieWeb.Movie("Avatar",
                        "A marine in West Philidelphia",
                        "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY")

pulp_fiction = MovieWeb.Movie("Pulp Fiction", "Shit goes down in West Philli",
                              "https://shyfyy.files.wordpress.com/2012/02/pulpfiction.jpg",
                              "https://www.youtube.com/watch?v=wZBfmBvvotE")

howl_moving_castle = MovieWeb.Movie("Howl's Moving Castle",
                        "A moving castle in West Phillidelphia",
                        "https://upload.wikimedia.org/wikipedia/en/a/a0/Howls-moving-castleposter.jpg",
                        "https://www.youtube.com/watch?v=iwROgK94zcM")

before_sunrise = MovieWeb.Movie("Before Sunrise",
                        "Two you people meet on a train to West Philidelphia",
                        "https://upload.wikimedia.org/wikipedia/en/d/da/Before_Sunrise_poster.jpg",
                        "https://www.youtube.com/watch?v=9v6X-Dytlko")

nightcrawler = MovieWeb.Movie("Nightcrawler",
                        "A man becomes a film maker West Philidelphia",
                        "https://upload.wikimedia.org/wikipedia/en/d/d4/Nightcrawlerfilm.jpg",
                        "https://www.youtube.com/watch?v=X8kYDQan8bw")

movies = [toy_story, avatar, pulp_fiction, howl_moving_castle, before_sunrise, nightcrawler]

#Opens the default browser and loads a page containing the listed information
fresh_tomatoes.open_movies_page(movies)

