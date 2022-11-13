import re
import nltk
from string import punctuation
from nltk.corpus import stopwords
russian_stopwords = stopwords.words("russian")
russian_stopwords.extend(
    ['это', "который", 'но', 'например',
        'которые', 'none']
)
punctuation = list(map(lambda i: i, punctuation))
# punctuation += "–»« \n\t".split("")
punctuation += ["\n", "\t", "-", "»", "«", " ", "\n ", " \t", "\t "]
rm_tag = re.compile('<.*?>')
rm_href = re.compile('[\d+]')
rm_short = re.compile('\w+\.')
rm_spaces = re.compile('\s+')

class HTMLCleaner:
    def __init__(self, text):
        self.text = text

    def action(self):
        return re.sub(rm_href, ' ', re.sub(rm_tag, '', self.text))


class RMSymbolsWords:
    def __init__(self, words):
        self.words = words

    def action(self):
        return filter(lambda i: i not in punctuation, self.words)


class RMStopWords:
    def __init__(self, words):
        self.words = words

    def action(self):
        return filter(lambda i: i not in russian_stopwords, self.words)
