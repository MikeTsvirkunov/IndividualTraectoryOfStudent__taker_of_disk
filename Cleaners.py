import nltk

class HTMLCleaner:
    def __init__(self, text):
        self.text = text

    def action(self):
        return re.sub(clean_raw, '', self.text)


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
