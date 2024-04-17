import requests
from bs4 import BeautifulSoup
import json

with open("input.txt", "r") as input_file:
    urls = input_file.readlines()

for idx, url in enumerate(urls):
    url = url.strip()
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    article = ""
    for data in soup.find_all("p"):
        article += data.get_text() + "\n"


    filename = f"article_{idx + 1}.txt"
    with open(filename, "w") as write_file:
        write_file.write(article)

    print(f"Article {idx + 1} saved to {filename}")

