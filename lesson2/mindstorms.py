import turtle

def draw_square(some_turtle):
	for i in range(1, 5):
		some_turtle.forward(100)  # steps
		some_turtle.right(90)  # degrees

def draw_art():
	window = turtle.Screen()
	window.bgcolor("red")

	# create the turtle Brad - draws a square
	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("green")
	brad.speed("slow")

	# draw a square 36 times, moving 10 degrees to the right each pass; squares carve out a circle
	for i in range(1, 37):
		# draw_square(brad)
		brad.circle(100)
		brad.right(10)	# degrees

	# create the turtle Angie - draws a circle
	# angie = turtle.Turtle()
	# angie.shape("arrow")
	# angie.color("blue")
	# angie.circle(100)

	window.exitonclick()

draw_art()