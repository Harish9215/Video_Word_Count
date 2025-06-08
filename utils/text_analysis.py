import re
from collections import Counter

def count_words(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words)

def search_word(word_counts, search_term):
    return word_counts.get(search_term.lower(), 0)
