import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = "https://www.fatafeat.com/"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all image tags
    img_tags = soup.find_all('img')
    
    # Extract and download images
    for img_tag in img_tags:
        img_url = img_tag.get('src')
        
        # Some URLs may be relative, so convert them to absolute URLs
        img_url = urljoin(url, img_url)
        
        # Download the image
        img_data = requests.get(img_url).content
        
        # Save the image with a unique name
        img_name = img_url.split("/")[-1]
        with open(img_name, 'wb') as img_file:
            img_file.write(img_data)
            
        print(f"Image {img_name} downloaded successfully.")

else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
