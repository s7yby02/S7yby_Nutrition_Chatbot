import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup


def add_data_to_json(tag, patterns, responses, json_file_path):
    # Load existing JSON data
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    # Add new data
    new_entry = {
        "tag": tag,
        "patterns": patterns,
        "responses": responses
    }

    data.append(new_entry)

    # Write updated data back to the JSON file
    with open(json_file_path, 'w') as file:
        json.dump(data, file, indent=2)





# Set up the Chrome WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode to avoid opening a browser window
driver = webdriver.Chrome(options=chrome_options)

# Load the website
url = "https://www.bodybuilding.com/"
driver.get(url)

# Wait for dynamic content to load (you might need to adjust the waiting time)
driver.implicitly_wait(5)

# Get the page source after dynamic content has loaded
page_source = driver.page_source

# Close the WebDriver
driver.quit()

# Parse the page source with BeautifulSoup
soup = BeautifulSoup(page_source, "html.parser")
try:
    # Extract data (replace these selectors with the actual ones from the website)
    tags = soup.select("#js-bbcom-app > div.BBCMS__container__header > div.BBCMS__content--title-bar > h1")
    patterns = soup.select(".#main > div.BBCMS__content--article-content > div")
    responses = soup.select("#main > div.BBCMS__content--article-content > div > p:nth-child(4)")
except Exception as e:
    print(f"An error occurred: {e}")

# Print the extracted data
for tag, pattern, response in zip(tags, patterns, responses):
    json_file_path= "Data_extracted.json"
    add_data_to_json(tag, patterns, responses, json_file_path )


