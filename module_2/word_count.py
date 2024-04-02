#This file (shockingly) counts the words in each article.
def count_words(articles):
    word_counts = []
    for idx, article in enumerate(articles):
        words = article.split()
        word_count = len(words)
        word_counts.append(word_count)

    return word_counts