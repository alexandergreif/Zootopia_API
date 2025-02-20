# Animal Data Website Generator

This project fetches animal data from an API and creates a simple website displaying the information.

## How to Run

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
Install dependencies: Make sure you have Python installed, then run:

bash
pip install -r requirements.txt
This will install both requests and python-dotenv.

Run the website generator:

bash
python animals_web_generator.py
You'll be prompted to enter an animal name (for example, "Fox"). The program will fetch the data and generate an animals.html file.

View the website: Open animals.html in your browser to see the results.

Project Structure
data_fetcher.py: Fetches animal data from the API.
animals_web_generator.py: Generates the website using the fetched data.
animals_template.html: HTML template for the website.
requirements.txt: Lists project dependencies.
README.txt: This file.
Feel free to explore and contribute!