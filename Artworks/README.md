
# Artworks Project

This repository contains Python scripts designed to manage and display information about artworks and their artists. There are two distinct setups within this project:

1. **Artworks Label.py**: A standalone script that encapsulates all the functionality needed to input, manage, and display artworks and artist information in a single file.
2. **Modular Approach**: Consists of three separate files (`main.py`, `artist.py`, and `artwork.py`) that work together to achieve the same functionality as `Artworks Label.py` but in a more modular and extensible manner.

## Artworks Label.py (Standalone)

`Artworks Label.py` is designed for simplicity and ease of use, combining all necessary classes and functions in a single file. This script is ideal for quick deployment or educational purposes where understanding the concept in a unified context is beneficial.

### Usage

To run the standalone script, simply execute it with Python:

```bash
python Artworks\ Label.py
```

Follow the on-screen prompts to enter information about artists and their artworks.

## Modular Approach (main.py, artist.py, artwork.py)

The modular approach separates concerns by dividing the functionality into three files:

- `artist.py`: Defines the `Artist` class, responsible for storing and managing artist-related information.
- `artwork.py`: Defines the `Artwork` class, responsible for handling artwork-related details, including a reference to an `Artist` object.
- `main.py`: Serves as the entry point of the program, facilitating user input and orchestrating the creation of `Artist` and `Artwork` objects based on that input.

### Usage

To use the modular approach, ensure that all three files (`main.py`, `artist.py`, `artwork.py`) are in the same directory. Run `main.py` with Python:

```bash
python main.py
```

Like with the standalone script, follow the prompts to input information about artists and artworks. The modular structure allows for easier maintenance, scalability, and reuse of the `Artist` and `Artwork` classes in different contexts.

## Getting Started

Clone this repository to your local machine to get started with either the standalone script or the modular approach:

```bash
git clone https://github.com/RIck-Abraham/Python-Projects.git
cd Python-Projects/Artworks
```

## Contributing

Contributions to enhance the functionality, improve the code structure, or fix bugs are always welcome. Please feel free to fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the `LICENSE` file in the root directory for details.
