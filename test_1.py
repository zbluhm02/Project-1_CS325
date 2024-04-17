import pytest
import json
import requests
from bs4 import BeautifulSoup

def test_passes_connection():
    """Tests if the connects to the webiste."""
    url = "https://apnews.com/article/fani-willis-hearing-trump-case-potential-conflict-c37fcf993ac33c150f3cb3e4a7a888db"
    url = url.strip()
    response = requests.options(url)
    assert response.status_code == 200



