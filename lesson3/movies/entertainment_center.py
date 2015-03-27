import fresh_tomatoes
import media

matrix = media.Movie(movie_title = "The Matrix",
					 movie_storyline = "Neo searches for the truth about the Matrix and discovers his place in it.", 
					 poster_image = "http://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg", 
					 trailer_youtube = "https://www.youtube.com/watch?v=_Ls19O-9p3s")

point_break = media.Movie(movie_title = "Point Break",
					     movie_storyline = "Reeves stars as rookie FBI agent Johnny Utah, who is investigating a string of bank robberies possibly being committed by surfers. Johnny goes undercover to infiltrate the surfing community and develops a complex friendship with Bodhi (Swayze), the charismatic leader of a gang of surfers.", 
					     poster_image = "http://upload.wikimedia.org/wikipedia/en/7/7e/Pointbreaktheatrical.jpg", 
					     trailer_youtube = "https://www.youtube.com/watch?v=AVk3mR2UhgI")

fight_club = media.Movie(movie_title = "Fight Club",
					     movie_storyline = "An insomniac office worker looking for a way to change his life crosses paths with a devil-may-care soap maker and they form an underground fight club that evolves into something much, much more...", 
					     poster_image = "http://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg", 
					     trailer_youtube = "www.youtube.com/watch?v=SUXWAEX2jlg")

usual_suspects = media.Movie(movie_title = "The Usual Suspects",
						     movie_storyline = "A sole survivor tells of the twisty events leading up to a horrific gun battle on a boat, which begin when five criminals meet at a seemingly random police lineup.", 
						     poster_image = "http://upload.wikimedia.org/wikipedia/en/9/9c/Usual_suspects_ver1.jpg", 
						     trailer_youtube = "https://www.youtube.com/watch?v=oiXdPolca5w")

apollo = media.Movie(movie_title = "Apollo 13",
					 movie_storyline = "The film depicts astronauts Lovell, Jack Swigert and Fred Haise aboard Apollo 13 for America's third Moon landing mission. En route, an on-board explosion deprives their spacecraft of most of its oxygen supply and electric power, forcing NASA's flight controllers to abort the Moon landing, and turning the mission into a struggle to get the three men home safely.", 
					 poster_image = "http://upload.wikimedia.org/wikipedia/en/9/9e/Apollo_thirteen_movie.jpg", 
					 trailer_youtube = "https://www.youtube.com/watch?v=nEl0NsYn1fU")

contact = media.Movie(movie_title = "Contact",
					  movie_storyline = "A SETI scientist who finds strong evidence of extraterrestrial life and is chosen to make first contact.", 
					  poster_image = "http://upload.wikimedia.org/wikipedia/en/7/75/Contact_ver2.jpg", 
					  trailer_youtube = "https://www.youtube.com/watch?v=d9C2cF3KvP8")


movies = [matrix, point_break, fight_club, usual_suspects, apollo, contact]
fresh_tomatoes.open_movies_page(movies)