from used_lib import *
from variables import *


class GetUrlText:
    def __init__(self, url):
        self.url = url

    def action(self):
        soup = BeautifulSoup(get(self.url,
                                 verify=False).text,
                             'html.parser')
        return ' '.join([str(i.string).lower() for i in soup.find_all('p')])


class HTMLCleaner:
    def __init__(self, text):
        self.text = text

    def action(self):
        return re.sub(clean_raw, '', self.text)


class GetCleanUrlText:
    def __init__(self, url):
        self.url = url

    def action(self):
        soup = BeautifulSoup(get(self.url,
                                 verify=False).text,
                             'html.parser')
        return ' '.join(
            map(lambda i: str(i.string).lower(), soup.find_all('p')))


class SplitOnSentences:
    def __init__(self, text):
        self.text = text

    def action(self):
        return self.text.split(". ")


class SplitOnWords:
    def __init__(self, text):
        self.text = text

    def action(self):
        return self.text.split(" ")


class SplitOnToken:
    def __init__(self, text):
        self.text = text

    def action(self):
        return nltk.word_tokenize(self.text)


class GetCombOfWord:
    def __init__(self, words, size=2):
        self.words = words
        self.size = size

    def action(self):
        return set(combinations(self.words, self.size))


class GetWordsTyped:
    def __init__(self, words, types):
        self.words = words
        self.types = types

    def action(self):
        return filter(lambda i: any(
            map(lambda j: j.tag.POS in self.types, morph.parse(i))), self.words)


class RMStopWords:
    def __init__(self, words):
        self.words = words

    def action(self):
        return filter(lambda i: i not in russian_stopwords, self.words)


class RMSymbolsWords:
    def __init__(self, words):
        self.words = words

    def action(self):
        return filter(lambda i: i not in punctuation, self.words)


class WordMaybeTypes:
    def __init__(self, word):
        self.word = word

    def action(self):
        return set(map(lambda i: i.tag.POS, morph.parse(self.word)))


class WordMaybeCases:
    def __init__(self, word):
        self.word = word

    def action(self):
        return set(map(lambda i: i.tag.case, morph.parse(self.word)))


class GetTypedPares:
    def __init__(self, words_pare, type1, type2):
        self.words_pare = words_pare
        self.type1 = type1
        self.type2 = type2

    def action(self):
        return filter(
            lambda i: (
                self.type1 in WordMaybeTypes(
                    i[0]).action() and self.type2 in WordMaybeTypes(
                    i[1]).action()) ^ (
                self.type2 in WordMaybeTypes(
                    i[0]).action() and self.type1 in WordMaybeTypes(
                    i[1]).action()),
            self.words_pare)


class GetConnectiablePares:
    def __init__(self, words_pares):
        self.words_pares = words_pares

    def action(self):
        return filter(lambda i: 0 < len(set(WordMaybeCases(i[0]).action()) & set(
            WordMaybeCases(i[1]).action())), self.words_pares)


class GetConnectiableLines:
    def __init__(self, words_lines):
        self.words_lines = words_lines

    def action(self):
        return filter(lambda i: all(map(lambda j: len(WordMaybeCases(i[0]).action() & 
            WordMaybeCases(j).action()), i)), self.words_lines)
