from bs4 import BeautifulSoup
import requests

r = requests.get("https://www.timeanddate.com/countdown/create")

data = r.text

soup = BeautifulSoup(data, 'html.parser')

# Get the list of all available themes
type_objs = soup.find(id="cd-templates")
theme_list = [];
for link in soup.find_all('article'):
	theme_list.append(link.get('data-theme'))

for theme in theme_list:
	if not theme == None:
		print(theme)

