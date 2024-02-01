# Define the Artist class to store and manage artist-related information
class Artist:
    def __init__(self, name, birth_year, death_year=None):
        self.name = name  # The name of the artist
        self.birth_year = birth_year  # The birth year of the artist
        self.death_year = death_year  # The death year of the artist, optional

    # Method to print information about the artist
    def print_info(self):
        # Check if the artist's death year is provided or if they are presumed alive
        if self.death_year is None or self.death_year == 'None':
            death_info = ' - '  # Use 'Present' to indicate the artist is still alive
        else:
            death_info = self.death_year  # Otherwise, use the provided death year
        # Print the artist's information
        print(f"Artist: {self.name} (Born: {self.birth_year}, Died: {death_info})")

# Define the Artwork class to store and manage artwork-related information
class Artwork:
    def __init__(self, title, year_created, artist):
        self.title = title  # The title of the artwork
        self.year_created = year_created  # The year the artwork was created
        self.artist = artist  # The artist who created the artwork

    # Method to print information about the artwork
    def print_info(self):
        print(f"Title: {self.title}, Year: {self.year_created}")
        self.artist.print_info()  # Print information about the artist

# Function to safely get user input, allowing for integer or 'None' values
def get_integer_input(prompt, allow_none=False):
    while True:
        user_input = input(prompt)  # Prompt the user for input
        # Check if 'None' is an acceptable value and if the user entered 'None' or left it blank
        if allow_none and (user_input.lower() == 'none' or user_input == ''):
            return None  # Return None to indicate no value was provided
        try:
            return int(user_input)  # Attempt to convert the input to an integer
        except ValueError:
            # If conversion fails, inform the user and prompt again
            print("Please enter a valid integer or 'None' if applicable.")

# Main block for executing the program logic
if __name__ == "__main__":
    # Collect artist information and artwork details from the user
    user_artist_name = input("Enter the artist's name: ")
    user_birth_year = get_integer_input("Enter the artist's birth year: ")
    # Allow 'None' for the artist's death year to accommodate living artists
    user_death_year = get_integer_input("Enter the artist's death year (or 'None' if still alive): ", allow_none=True)
    user_title = input("Enter the artwork's title: ")
    user_year_created = get_integer_input("Enter the year the artwork was created: ")

    # Create an Artist object with the user-provided information
    user_artist = Artist(user_artist_name, user_birth_year, user_death_year)
    # Create an Artwork object with the artwork details and associated Artist object
    new_artwork = Artwork(user_title, user_year_created, user_artist)

    # Print detailed information about the newly created artwork
    new_artwork.print_info()
