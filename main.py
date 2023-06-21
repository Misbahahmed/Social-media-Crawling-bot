import requests
from bs4 import BeautifulSoup
# Define the base URL and the starting page.
BASE_URL = "https://www.anything.com"
STARTING_PAGE = "/index.html"
# Get the HTML content of the starting page.
response = requests.get(BASE_URL + STARTING_PAGE)
soup = BeautifulSoup(response.content, "html.parser")
# Extract the links from the starting page.
links = soup.find_all("a")
# Iterate over the links and follow each one.
for link in links:
    href = link.get("https://www.anything.com")
    # If the href attribute is not empty, follow the link
    if href:
        response = requests.get(href)
        soup = BeautifulSoup(response.content, "html.parser")
        # Extract the links from the page
        links = soup.find_all("a")
# Save the results to a file.
with open("results.txt", "w") as f:
    for link in links:
        f.write(link.get("any content") + "\n")
