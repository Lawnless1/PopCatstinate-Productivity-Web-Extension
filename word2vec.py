import os
script_dir = os.path.dirname(os.path.abspath(__file__))
from gensim.models import KeyedVectors


isLoaded = False


def get_productivity_score(website, title):
    if (isLoaded == False):
        filename = os.path.join(script_dir, 'GoogleNews-vectors-negative300.bin')
        model = KeyedVectors.load_word2vec_format(filename, binary=True)
        isLoaded = True
                
    list_of_productivity_words = ["productive", "useful", "help", "productivity", "goal", "learn"]

    title = title.strip().split()
    Pass = False
    longest_word = None
    sum_of_productivity_words = 0
    if len(title) == 0:
        Pass = True
    if len(title) > 1:
        max = 0
        for word in title:
            if len(word) > max:
                max = len(word)
                longest_word = word
    if longest_word:
        if len(longest_word) == 1:
            longest_word = title[0]
        elif not Pass:
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