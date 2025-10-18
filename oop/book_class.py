class Book:
    def __init__(self, title: str, author: str, year: int):
        """
        Constructor to initialize the Book instance.
        """
        self.title = title
        self.author = author
        self.year = year
     def __del__(self):
        """
        Destructor to handle object deletion.
        """
        print(f"Deleting {self.title}")
    def __str__(self):
        """
        Informal string representation of the Book instance.
        """
        return f"{self.title} by {self.author}, published in {self.ear}"
    def __repr__(self):
        """
        Official string representation of the Book instance.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"
