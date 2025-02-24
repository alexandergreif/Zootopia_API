# Animal Data Website Generator

This project fetches animal data from an API and generates a website to display the information. The code is split into two main parts:

- **Data Fetcher:** Fetches animal data from the API.
- **Website Generator:** Generates the HTML website using the fetched data.

## How It Works

1. **Data Fetcher:**  
   The module `data_fetcher.py` contains the `fetch_data` function, which takes an animal name (e.g., "Fox") as input, makes an API call, and returns a list of animal dictionaries.

2. **Website Generator:**  
   The module `animals_web_generator.py` uses the data fetched by the data fetcher to build an HTML page. It reads an HTML template (`animals_template.html`), replaces a placeholder with serialized animal data, and writes the final output to `animals.html`.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
Install Dependencies: Make sure you have Python installed, then run:
bash
pip install -r requirements.txt
This will install both requests and python-dotenv.
Usage
Run the website generator:

bash
python animals_web_generator.py
The script will prompt you to enter an animal name.
It fetches the data from the API and generates an animals.html file.
Open animals.html in your browser to view the website.
Project Structure
data_fetcher.py: Handles fetching animal data from the API.
animals_web_generator.py: Generates the website using the fetched data.
animals_template.html: HTML template for the website.
animals.html: The generated website file.
requirements.txt: Project dependencies.
README.md: This file.
Contributing
Contributions are welcome! Feel free to fork the repository and submit pull requests with improvements or bug fixes.