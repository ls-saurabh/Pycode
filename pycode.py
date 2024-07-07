import requests

def viewPage(url):
    response = requests.get(url)
    if response.status_code == 200:
        print(response.text)
    else:
        print(f"Failed to retrieve page: {response.status_code}")

# Prompt the user to enter a URL
url = input("Enter URL: ")
viewPage(url)