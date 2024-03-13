#This file processes and strips the news articles and returns them to the run.py file.
#It expects file path (to find a file the contains string urls) as input.
import requests
from bs4 import BeautifulSoup

def urls(input_file_path):
    with open(input_file_path, "r") as input_file:
        urls = input_file.readlines()

    articles = []
    for idx, url in enumerate(urls):
        url = url.strip()
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')

        article = ""
        for data in soup.find_all("p"):
            article += data.get_text() + "\n"
        articles.append(article)

    return articles