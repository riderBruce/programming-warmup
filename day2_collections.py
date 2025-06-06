
# Practice with the following:
# A list of 5 favorite movies (add, remove, sort)
favorite_movies_list = ["Vanilla Sky", "The Intern", "Crazy Stupid Love", "Like Crazy", "Mama Mia"]
favorite_movies_list.append("Notebook")
print(favorite_movies_list)
for s in favorite_movies_list:
    print(s)
favorite_movies_list.remove("Mama Mia")
print(favorite_movies_list)
for s in favorite_movies_list:
    print(s)
favorite_movies_list.sort()
print(favorite_movies_list)
for s in favorite_movies_list:
    print(s)

# A tuple with your birth year, month and day
my_birth = (1978, 7, 24)
print("My birth of year:", my_birth[0], ", month :", my_birth[1], ", day :", my_birth[2])
print(f"My birth of year: {my_birth[0]} , month : {my_birth[1]}, day : {my_birth[2]}")

# A dictionary representing a book: title, author, year, genre
my_books = {
    "sapiens": {"author": "Yuval Noa Harari", "year": 2011, "genre": "History"},
    "The Moon and Sixpence": {"author": "Somerset Maugham", "year": 1919, "genre": "Novel"}
}
print(my_books)
for title, info in my_books.items():
    print(f"Title : {title}")
    print(f"author : {info['author']}, year : {info['year']}, genre : {info['genre']}")


# Print the outputs and experiment with each data type.
