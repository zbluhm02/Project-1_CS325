import pytest
import json
import os
import requests
from bs4 import BeautifulSoup

from module_2 import word_count

def test_correct_count():
    #check for count accuracy
    #sample count is 985, should equal that
    url = "https://apnews.com/article/fani-willis-hearing-trump-case-potential-conflict-c37fcf993ac33c150f3cb3e4a7a888db"
    url = url.strip()
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    article = ""
    for data in soup.find_all("p"):
        article += data.get_text() + "\n"

    filename = "Data/processed/article.txt"
    with open(filename, "w") as write_file:
            write_file.write(article)
    
    words = article.split()
    word_count = len(words)
    
    assert word_count == 985