import media

toy_story = media.Movie(movie_title = "Toy Story",
						movie_storyline = "A story of a boy and his toys that come to life.", 
						poster_image = "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", 
						trailer_youtube = "https://www.youtube.com/watch?v=KYz2wyBy3kc")
print(toy_story.storyline)

avatar = media.Movie(movie_title = "Avatar",
					 movie_storyline = "A marine on an alien planet.", 
					 poster_image = "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg", 
					 trailer_youtube = "https://www.youtube.com/watch?v=cRdxXPV9GNQ")
print(avatar.storyline)

matrix = media.Movie(movie_title = "The Matrix",
					 movie_storyline = "Neo searches for the truth about the Matrix and discovers his place in it.", 
					 poster_image = "http://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg", 
					 trailer_youtube = "https://www.youtube.com/watch?v=_Ls19O-9p3s")
matrix.show_trailer()


