from bs4 import BeautifulSoup
import requests

r = requests.get("https://www.timeanddate.com/countdown/create")

data = r.text

soup = BeautifulSoup(data, 'html.parser')

# Get the list of all available themes
type_objs = soup.find(id="cd-templates")
for link in soup.find_all('article'):
    print(link.get('data-theme'))
