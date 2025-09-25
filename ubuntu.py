import os
import requests
from urllib.parse import urlparse

# Prompt user for image URL
url = input("Enter the URL of the image to fetch: ")

# Create directory 'Fetched_Images' if it doesn't exist
os.makedirs('Fetched_Images', exist_ok=True)

try:
    # Fetch the image
    response = requests.get(url)
    response.raise_for_status()  # Raise HTTPError for bad responses

    # Extract filename from URL
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)

    # Fallback filename if none found
    if not filename:
        filename = "fetched_image.jpg"

    # Full path to save the image
    image_path = os.path.join('Fetched_Images', filename)

    # Save image in binary mode
    with open(image_path, 'wb') as f:
        f.write(response.content)

    print(f"Image successfully saved to {image_path}")

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except requests.exceptions.RequestException as req_err:
    print(f"Error fetching the image: {req_err}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
