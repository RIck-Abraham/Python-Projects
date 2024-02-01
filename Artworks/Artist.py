class Artist:
    def __init__(self, name=None, birth_year=None, death_year=None):
        # Initialize the artist with name, birth year, and optionally death year
        self.name = name
        self.birth_year = birth_year
        self.death_year = death_year

    def print_info(self):
        # Determine the death info, using 'Present' if the artist is still alive
        death_info = ' - ' if self.death_year is None else self.death_year
        # Print the artist's information in a readable format
        print(f"Artist: {self.name}, Born: {self.birth_year}, Died: {death_info}")
