
# Artwork and Artist Information Manager

This Python script provides classes `Artist` and `Artwork` to store and manage information related to artists and their artworks. It allows users to input data about artists and artworks, and then displays the collected information.

## Features

- **Artist Information**: Store and manage artist names, birth years, and death years (if applicable).
- **Artwork Information**: Keep track of artwork titles, creation years, and the artists who created them.
- **User Input**: Collect information from users about artists and artworks through a simple command-line interface.
- **Data Display**: Neatly print out collected information, linking artworks to their respective artists.

## Getting Started

To use this script, you can clone the repository or simply copy the provided classes and functions into your Python project.

### Prerequisites

You need to have Python installed on your system. This script is compatible with Python 3.x.

### Installation

To get a local copy up and running, follow these simple steps:

```bash
git clone https://github.com/yourusername/your-repository.git
```

### Usage

After cloning or copying the script, run it from the command line:

```bash
python your_script_name.py
```

Follow the prompts to enter information about an artist and an artwork. The script will then display the information you've entered.

### Example

When you run the script, you will be prompted to enter information like this:

```
Enter the artist's name: Vincent van Gogh
Enter the artist's birth year: 1853
Enter the artist's death year (or 'None' if still alive): 1890
Enter the artwork's title: The Starry Night
Enter the year the artwork was created: 1889
```

The script will then output:

```
Title: The Starry Night, Year: 1889
Artist: Vincent van Gogh (Born: 1853, Died: 1890)
```

## Contributing

Contributions are welcome! If you have ideas on how to improve this script or add new features, please feel free to contribute.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/YourFeature`)
3. Commit your Changes (`git commit -m 'Add some YourFeature'`)
4. Push to the Branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
