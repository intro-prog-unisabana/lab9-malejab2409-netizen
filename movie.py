# Write your code here!
# FREEZE CODE BEGIN
class Movie:
    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year
# FREEZE CODE END
    def _str_(self):
        return f"Movie: {self.title} (Directed by {self.director}, {self.year})"
        print()

# FREEZE CODE BEGIN
if __name__ == "__main__":
    # --- Main Program ---
    title = input("Enter the movie title: ")
    director = input("Enter the director's name: ")
    year = input("Enter the release year: ")
# FREEZE CODE END
    
    
    # TODO: Construct a Movie object!
    # TODO: Print the object!
