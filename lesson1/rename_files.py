import os

def rename_files():

	file_path = "./data/prank"

	# 1. get the filenames from a folder
	file_list = os.listdir(file_path)
	
	saved_path = os.getcwd()

	# 2. for each file, renmae filenames
	os.chdir(file_path)
	for file_name in file_list:
		new_file_name = file_name.translate(None, "0123456789")  # new filename without numbers		
		print("Old name - {}".format(file_name))
		print("New name - {}".format(new_file_name))		
		print("")
		os.rename(file_name, new_file_name)

	os.chdir(saved_path)

rename_files()