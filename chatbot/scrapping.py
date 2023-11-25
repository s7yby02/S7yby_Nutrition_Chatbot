
import requests
from bs4 import BeautifulSoup

def scrape_and_save(url, filename):
     response = requests.get(url)

     if response.status_code == 200:
         soup = BeautifulSoup(response.text, 'html.parser')

         # Find all paragraphs within the class "ContentPage"
         content_paragraphs = soup.find('div', class_='ContentPage')  # Replace 'ContentPage' with the actual class name

         if content_paragraphs:
             # Extract text from each paragraph
             paragraphs_text = [p.get_text(strip=True) for p in content_paragraphs.find_all('p')]

             # Save the paragraphs to a file
             with open(filename, "a", encoding="utf-8") as text_file:
                 text_file.write('\n\n'.join(paragraphs_text))

             print(f"Paragraphs from {url} scraped successfully and saved to '{filename}'.")

         else:
             print(f"Class 'ContentPage' not found on {url}.")

     else:
         print(f"Failed to retrieve the webpage {url}. Status code: {response.status_code}")

if __name__ == "__main__":
     starting_url = "https://www.bodybuilding.com/content/meal-plan-for-every-guy.html"
     output_filename = "healthline_paragraphs.txt"
    
     # Clear the existing content of the output file
     with open(output_filename, "w", encoding="utf-8"):
         pass

     # Start scraping from the starting URL
     scrape_and_save(starting_url, output_filename)
    



# import time
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service as ChromeService
# from urllib.parse import urljoin
# import requests

# def scrape_and_save(url, filename):
#     response = requests.get(url)

#     if response.status_code == 200:
#         soup = BeautifulSoup(response.text, 'html.parser')

#         # Find all paragraphs within the class "ContentPage"
#         content_paragraphs = soup.find('div', class_='ContentPage')  # Replace 'ContentPage' with the actual class name

#         if content_paragraphs:
#             # Extract text from each paragraph
#             paragraphs_text = [p.get_text(strip=True) for p in content_paragraphs.find_all('p')]

#             # Save the paragraphs to a file
#             with open(filename, "a", encoding="utf-8") as text_file:
#                 text_file.write('\n\n'.join(paragraphs_text))

#             print(f"Paragraphs from {url} scraped successfully and saved to '{filename}'.")

#             # Find all links on the page and follow them
#             for link in content_paragraphs.find_all('a', href=True):
#                 next_url = urljoin(url, link['href'])
#                 scrape_and_save(next_url, filename)

#         else:
#             print(f"Class 'ContentPage' not found on {url}.")

#     else:
#         print(f"Failed to retrieve the webpage {url}. Status code: {response.status_code}")

# def selenium_search_and_scrape(query):
#     search_url = "https://www.healthline.com/search?q=" + query

#     # Set up the WebDriver (replace 'path/to/chromedriver' with the actual path)
#     chrome_path = "C:\Users\ABDELLAH\Desktop\S7yby_Nutrition_Chatbot\chromedriver"
#     service = ChromeService(chrome_path)
#     driver = webdriver.Chrome(service=service)

#     try:
#         # Open the search page
#         driver.get(search_url)
#         time.sleep(2)  # Wait for the page to load

#         # Execute Selenium code here
#         # For example, click on the first search result link
#         first_result = driver.find_element("css selector", ".search-list-item a")
#         first_result.click()

#         # Wait for the page to load
#         time.sleep(2)

#         # Scrape paragraphs using BeautifulSoup
#         current_url = driver.current_url
#         scrape_and_save(current_url, "healthline_paragraphs_all_pages.txt")

#     finally:
#         # Close the WebDriver
#         driver.quit()

# if __name__ == "__main__":
#     selenium_search_and_scrape("vitamin D")
        