"""
A simple function.

Create a simple function called favorite_movie, which takes a string containing the name of your favorite movie.
The function should then print "My favorite movie is named {name}".
"""


def favorite_movie(name: str) -> str:
    return f"My favorite movie is named {name}"


print(favorite_movie('Se7en'))
