import requests
from bs4 import BeautifulSoup

url = "https://fr.wikipedia.org/wiki/Liste_des_genres_de_fourmis"

response = requests.get(url)

soup_parser = BeautifulSoup(response.text,'html.parser')

ant_type = []

for i in soup_parser.find_all(class_="new") :
    print(i.get_text())
    ant_type.append(i.get_text())

print(ant_type)