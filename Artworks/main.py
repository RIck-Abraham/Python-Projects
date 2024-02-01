from Artist import Artist  # Import the Artist class
from Artwork import Artwork  # Import the Artwork class

def get_input(prompt, expected_type=int, allow_none=False):
    while True:
        user_input = input(prompt)
        if allow_none and user_input.lower() == 'none':
            return None  # Allow 'None' as a valid input if specified
        try:
            return expected_type(user_input)  # Convert the input to the expected type
        except ValueError:
            print(f"Invalid input, please enter a {expected_type.__name__} or 'None' if allowed.")

if __name__ == "__main__":
    # Collect artist information from the user
    user_artist_name = input("Enter the artist's name: ")
    user_birth_year = get_input("Enter the artist's birth year: ")
    user_death_year = get_input("Enter the artist's death year (or 'None' if still alive): ", allow_none=True)

    # Collect artwork information from the user
    user_title = input("Enter the artwork's title: ")
    user_year_created = get_input("Enter the year the artwork was created: ")

    # Create an Artist instance with the provided information
    user_artist = Artist(user_artist_name, user_birth_year, user_death_year)
    # Create an Artwork instance with the provided information and associated Artist
    new_artwork = Artwork(user_title, user_year_created, user_artist)

    # Print detailed information about the artwork and the artist
    new_artwork.print_info()
