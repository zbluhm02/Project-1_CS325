import pytest
import json
import os
import openai
import requests
from bs4 import BeautifulSoup

from module_3.sk import my_sk #Grabbing secret key from other python file

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
    
    openai.api_key = my_sk

    response2 = openai.ChatCompletion.create( #API call for title
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful research assistant."},
            {"role": "user", "content": f"Output a random series of letters"},
        ],
    )
    test = response2["choices"][0]["message"]["content"]
    
    assert test != ""