import urllib

def read_text():
	quotes = open("movie_quotes.txt")
	contents_of_file = quotes.read()
	quotes.close()
	check_profanity(contents_of_file)

def check_profanity(text_to_check):
	# Google's "What Do You Love" website
	base_url = "http://www.wdyl.com/profanity"
	query_str = "?q=" + text_to_check
	connection = urllib.urlopen(base_url + query_str)
	output = connection.read()
	connection.close()
	if "true" in output:
		print("Profanity Alert!!")
	elif "false" in output:
		print("This document has no curse words!")
	else:
		print("Cound not scan the document properly.")

read_text()