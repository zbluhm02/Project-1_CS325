import pytest
import json
import requests
from bs4 import BeautifulSoup

def test_print_article():
    """Tests if it outputs a cleaned article."""
    url = "https://apnews.com/article/fani-willis-hearing-trump-case-potential-conflict-c37fcf993ac33c150f3cb3e4a7a888db"
    url = url.strip()
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    article = ""
    for data in soup.find_all("p"):
        article += data.get_text() + "\n"
    assert article != ""



