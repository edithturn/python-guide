# LISTS
print("==== Lists ====")
movies = ["The Holy Grail", "The Life of Brail", "The Meaning of Life"]
# Insert a element in a specific location in the array
movies.insert(1, 1978)
movies.insert(3, 1979)
# Add a new element at the end of the list
movies.append(1983)
# Recreating the list
movies1 = ["The Holy Grail", 1978, "The Life of Brail", 1979, "The Meaning of Life", 1983]
print(movies)
print(movies1)

# ITERATE
fav_movies = ["the Holy Grail", "The Life of Brian"]

print("==== For ====")
for each_flick in fav_movies:
	print(each_flick)

print("==== While ====")
count = 0
while count < len(movies):
	print(movies[count])
	count += 1

# Store lists within lists
print("==== List within list ====")
movies = ["the Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91, ["Graham Chapman", ["Michael Pain", ["Single", 37, "Germany"], "John Cleese", "terry Gilliam", "Eric Idle", "Terry Jones"]]]
print(movies[4][1][3])

print("==== For Loops List Within List ====")
for each_item in movies:
	if (isinstance(each_item, list)):
		for nested_item in each_item:
			if (isinstance(nested_item, list)):
				for core_item in nested_item:
					if(isinstance(core_item, list)):
						for deepest_item in core_item:
							print( "    ", deepest_item)
					else:
						print("   ", core_item)
			else:
				print("  ", nested_item)
	else:
		print(" ",each_item)

