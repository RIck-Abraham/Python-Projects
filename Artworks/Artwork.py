from Artist import Artist  # Import the Artist class to associate an artist with an artwork

class Artwork:
    def __init__(self, title=None, year_created=None, artist=None):
        # Initialize the artwork with a title, creation year, and artist
        self.title = title
        self.year_created = year_created
        self.artist = artist

    def print_info(self):
        # Print the artwork's title and year of creation
        print(f"Title: {self.title}, Year: {self.year_created}")
        # If an artist is associated with the artwork, print the artist's info
        if self.artist:
            self.artist.print_info()
        else:
            print("Unknown Artist")
