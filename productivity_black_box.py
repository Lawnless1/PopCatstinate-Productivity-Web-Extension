#imports
from word2vec import get_productivity_score

# open list of 1000 already scored websites
from dictionary1000 import dict1

# extract domain from url
import tldextract




def productivity_constant(website, title):
    website_extract = tldextract.extract(website)
    domain = website_extract.domain.lower()
    if domain in dict1:
        return dict1[domain]
    else:
        return round(get_productivity_score(website, title), 2)

