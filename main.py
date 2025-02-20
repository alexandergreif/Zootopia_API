import data_fetcher


def serialize_animal(animal_obj):
    """Serialize a single animal object into an HTML list item."""
    output = '<li class="cards__item">\n'

    # Serialize the animal's name in a dedicated title div
    if animal_obj.get("name"):
        output += f'  <div class="card__title">{animal_obj["name"]}</div>\n'

    output += '  <p class="card__text">\n'

    # Serialize Diet if available
    if animal_obj.get("characteristics") and animal_obj["characteristics"].get("diet"):
        output += (f'      <strong>Diet:</strong> '
                   f'{animal_obj["characteristics"]["diet"]}<br/>\n')

    # Serialize the first Location if available
    if animal_obj.get("locations") and animal_obj["locations"]:
        output += (f'      <strong>Location:</strong> '
                   f'{animal_obj["locations"][0]}<br/>\n')

    # Serialize Type if available
    if animal_obj.get("characteristics") and animal_obj["characteristics"].get("type"):
        output += (f'      <strong>Type:</strong> '
                   f'{animal_obj["characteristics"]["type"]}<br/>\n')

    output += "  </p>\n"
    output += "</li>\n"
    return output



def main():
    """Fetch animal data from the API, generate HTML output, and write it to a file."""
    user_animal = input("Please enter the animal your looking for: ")
    animals = data_fetcher.fetch_data(user_animal)

    animals_output = ""
    if not animals:
        animals_output = f'<h2>The animal "{user_animal}"does not exist. </h2>'
    else:
        # Build the HTML string using the serialize_animal function
        for animal in animals:
            animals_output += serialize_animal(animal)

    # Read the HTML template file
    template_file_path = "animals_template.html"
    with open(template_file_path, "r", encoding="utf-8") as template_file:
        template_content = template_file.read()

    # Replace the placeholder with the generated animals HTML
    new_html_content = template_content.replace("__REPLACE_ANIMALS_INFO__", animals_output)

    # Write the new HTML content to a file
    output_file_path = "animals.html"
    with open(output_file_path, "w", encoding="utf-8") as output_file:
        output_file.write(new_html_content)

    print("The animals.html file has been created successfully!")


if __name__ == "__main__":
    main()