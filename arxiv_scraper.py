# Import necessary modules
import requests
from bs4 import BeautifulSoup
import json
import os

# Set initial and final dates for article search
init_date = "2023-05-22"
final_date = "2023-05-28"

# Construct url using f-strings with specified search parameters
url = f'https://arxiv.org/search/advanced?advanced=&terms-0-operator=AND&terms-0-term=%22Reinforcement+Learning%22&terms-0-field=all&terms-1-operator=AND&terms-1-term=&terms-1-field=all&classification-physics_archives=all&classification-include_cross_list=exclude&date-year=&date-filter_by=date_range&date-from_date={init_date}&date-to_date={final_date}&date-date_type=submitted_date_first&abstracts=show&size=200&order=-announced_date_first'

# Make a GET request to the url and parse the html response into a soup object
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')

# Find all list items with class "arxiv-result" in the soup object and save them to the 'all' variable
all = soup.find_all('li', class_="arxiv-result")

# Define a function 'extract_info' to extract the title, abstract, and pdf link from a given result
def extract_info(result):

    # Extract the title and strip whitespace
    title = result.find_all(class_="title")[0].text.strip()

    # Extract the full abstract and strip whitespace
    abstract_full = result.find_all(class_="abstract-full")[0].text.strip()
    
    # Find all instances of the text "pdf" in the result
    pdf_links = result.find_all(text = "pdf")

    # If there is at least one pdf link, extract the href attribute of the parent element of the first instance
    # of the text "pdf"; otherwise, set pdf_link to an empty string
    pdf_link = pdf_links[0].parent.get("href") if len(pdf_links) >= 1 else ""

    # Return a tuple containing the title and a dictionary with the pdf link and abstract
    return title, {"link": pdf_link, "abstract": abstract_full, "string": f"[{title}]({pdf_link})"}

# Map the 'extract_info' function to all elements in the 'all' variable and save the results in a dictionary 'final_dict'
final_dict = dict(map(extract_info, all))

# Create a directory with the name of the final date (if it doesn't already exist) and write the 'final_dict' to a json file within that directory
dir = final_date.replace("-", "")

os.makedirs(f"./{dir}", exist_ok=True)
with open(f'{dir}/{dir}.json', 'w') as convert_file:
     convert_file.write(json.dumps(final_dict, indent=4, sort_keys=True))

print (len(final_dict))
