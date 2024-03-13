#This file is the run file which calls both the url (file that proccesses the urls) and the word count (file that counts the words in each article).
#It contains print statements for both saving the articles and the word count in the terminal. It also saves the articles to there own seperate files.
#This program applies the single responsibility principle as each module contains only one main purpose. The run file gathers outputed data and outputs it, the url file generates usable data from the websites, and the word count file counts the words in each file. 
import json
from module_1.url import urls
from module_2.word_count import count_words

def save(articles):
    for idx, article in enumerate(articles):
        filename = "Data/processed/article_%d.txt" % (idx + 1)
        with open(filename, "w") as write_file:
            write_file.write(article)
        print("Article %d saved to %s" % (idx + 1, filename))

def main():
    input_file_path = "Data/raw/input.txt"
    articles = urls(input_file_path)
    save(articles)

    word_counts = count_words(articles)
    print(json.dumps(word_counts, indent=2))

if __name__ == "__main__":
    main()
