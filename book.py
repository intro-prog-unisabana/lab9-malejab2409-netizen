class Book:
    def __init__(self, title, author, year):
        self._title = title  # Use _ to indicate private attribute
        self._author = author
        self._year = year

    # Getter for title
    def get_title(self):
        return self._title

    # Setter for title
    def set_title(self, title):
        if len(title) > 1:
            self._title = title
        else:
            print("Title is too short!")

    def __str__(self):
        return f"'{self._title}' by {self._author} ({self._year})"
