"""
This is nested.py module, and it provides one function called print_list(), 
which prints lists that may or may not nested lists
"""
def print_list(my_list):
"""
This function takes a positional argument calles my_listm which is any Python list.Each data item in the
provides list is recursively printed to the screen on its own line
"""
	for item in my_list:
		if (isinstance(item, list)):
			print_list(item)
		else:
			print(item)

"""
The main function to call the print_list function
"""
if __name__ == "__main__":
	print("=== Recursive Function ===")
	movies = ["the Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91, ["Graham Chapman", ["Michael Pain", ["Single", 37, "Germany"], "John Cleese", "terry Gilliam", "Eric Idle", "Terry Jones"]]]
	print_list(movies)