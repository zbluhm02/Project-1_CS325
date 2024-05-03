# This file is the run file which calls both the url (file that proccesses the urls) and the word count (file that counts the words in each article).
# It contains print statements for both saving the articles and the word count in the terminal. It also saves the articles to there own seperate files.
# This program applies the single responsibility principle as each module contains only one main purpose. The run file gathers outputed data and outputs it, the url file generates usable data from the websites, and the word count file counts the words in each file. 
#import json
#import openai
from xml.etree import ElementTree as ET
#from module_1.url import urls
#from module_2.word_count import count_words
#from module_3.sk import my_sk #Grabbing secret key from other python file


def save(articles): # Saves articles to the proccessed folder
    for idx, article in enumerate(articles):
        filename = "Data/processed/article_%d.txt" % (idx + 1)
        with open(filename, "w") as write_file:
            write_file.write(article)
        print("Article %d saved to %s" % (idx + 1, filename))

def summarize(articles):  # Saves summarized articles to the processed folder
    filename = "Data/summarized/summarized_articles.txt"
    for idx, article in enumerate(articles):
        with open(filename, "a") as write_file:
            openai.api_key = my_sk

            response2 = openai.ChatCompletion.create( #API call for title
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful research assistant."},
                    {"role": "user", "content": f"Output a title that would be best for this article: {article}. Make sure to only the title itself, not quotation marks or title headers"},
                ],
            )
            title = response2["choices"][0]["message"]["content"]
            write_file.write(title)
            write_file.write("\n")

            response = openai.ChatCompletion.create( #API call for summmarization
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful research assistant."},
                    {"role": "user", "content": f"Summarize this article around 50 words: {article}"},
                ],
            )
            page_summary = response["choices"][0]["message"]["content"]
            write_file.write(page_summary)
            write_file.write("\n\n")
            print("Summarized article saved to summarized folder.")


def txt_to_html(txt_file, html_file):
  """
  Converts a text file with header and paragraph to an HTML file.

  Args:
      txt_file (str): Path to the text file.
      html_file (str): Path to the output HTML file.
  """
  # Read text file content
  with open(txt_file, 'r') as f:
    content = f.read().strip().split("\n\n")
  
  # Create root element for HTML, try to remember the structure of a HTML file
  root = ET.Element("html")

  # Create head and body elements, try to understand how subElements works
  head = ET.SubElement(root, "head")
  title = ET.SubElement(head, "title")
  title.text = "Random Aggregation of Summarized News Articles"
  body = ET.SubElement(root, "body")

  for section in content:
    lines = section.strip().split("\n")
    if len(lines) < 2:
       continue

    header = lines[0].strip()
    paragraph = " ".join(lines[1:]).strip()

    # Create header and paragraph elements in body
    h1 = ET.SubElement(body, "h1")
    h1.text = header
    p = ET.SubElement(body, "p")
    p.text = paragraph

  # Write HTML tree to file
  tree = ET.ElementTree(root)
  tree.write(html_file, encoding='utf-8', xml_declaration=True, method='html')



def main():
    

    #input_file_path = "Data/raw/input.txt"
    #articles = urls(input_file_path)
    #save(articles)
    
    #word_counts = count_words(articles)
    #print(json.dumps(word_counts, indent=2))

    #summarize(articles)

    txt_file = "summarized_articles.txt"
    html_file = "aggregation.html"
    txt_to_html(txt_file, html_file)
    print("HTML file made.")

if __name__ == "__main__":
    main()
