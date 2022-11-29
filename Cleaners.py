import re
import nltk
from string import punctuation
from nltk.corpus import stopwords
russian_stopwords = stopwords.words("russian")
russian_stopwords.extend(
    ['это', "который", 'но', 'например',
        'которые', 'none', "на", 'со', 'не', 'в']
)
punctuation = list(map(lambda a: a, punctuation))
punctuation += ["\n", "\t", "-", "»", "«", " ", '—']
rm_tag = re.compile('<.*?>')
rm_href = re.compile('\[.+\]')
rm_short = re.compile('\w+\.')
rm_spaces = re.compile('\s+')
rm_add = re.compile('\(.+\)')


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


class CleanText:
    def __init__(self, text, bad_patterns = [rm_href, rm_add]):
        self.text = text.replace("\n", " ")
        self.bp = bad_patterns
    
    def action(self):
        for i in self.bp:
            self.text = re.sub(i, ' ', self.text)
        self.text = re.sub(rm_spaces, ' ', self.text)
        return self.text
