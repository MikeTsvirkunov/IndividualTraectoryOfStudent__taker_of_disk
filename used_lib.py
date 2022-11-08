import nltk
from numpy import array
from itertools import combinations
from requests import get
import re
import pymorphy2
from bs4 import BeautifulSoup
import urllib3
from nltk.corpus import stopwords
from string import punctuation

urllib3.disable_warnings()
russian_stopwords = stopwords.words("russian")
russian_stopwords.extend(
    ['это', "который", 'он', 'например', 'которые', 'none']
)
punctuation += "–»«"
# nltk.download('punkt')
