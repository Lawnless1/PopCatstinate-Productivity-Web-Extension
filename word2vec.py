import os
script_dir = os.path.dirname(os.path.abspath(__file__))
from gensim.models import KeyedVectors
filename = os.path.join(script_dir, 'GoogleNews-vectors-negative300.bin')
model = KeyedVectors.load_word2vec_format(filename, binary=True)

def get_productivity_score(website, title):
    list_of_productivity_words = ["productive", "useful", "help", "productivity", "goal", "learn"]

    title = title.strip().split()
    if len(title) > 1:
        max = 0
        for word in title:
            if len(word) > max:
                max = len(word)
                longest_word = word
    else:
        longest_word = title[0]
    sum_of_productivity_words = 0
    for word in list_of_productivity_words:
        try:
            a = model.similarity(longest_word, word)
            if a > sum_of_productivity_words:
                sum_of_productivity_words = a
        except KeyError:
            pass
                


    try:
        


        for productivitycompare in list_of_productivity_words:
            try:
                a = model.similarity(website, word)
                if a > sum_of_productivity_words:
                    sum_of_productivity_words = a
            except KeyError:
                pass


        return sum_of_productivity_words
    except Exception:
        if sum_of_productivity_words == 0:
            return 0
        else:
            return sum_of_productivity_words