from ParseToken import *
from Spliters import SplitOnWords
import spacy
from spacy import displacy


class ParseTokensOnTags:
    def __init__(self, sentence, language="ru_core_news_sm"):
        self.sentence = sentence
        self.nlp = spacy.load(language)

    def action(self):
        return list(
                    map(
                        lambda a: ParseTokenOnTags(a).action(), 
                        filter(
                              lambda a: a.text not in russian_stopwords, 
                              self.nlp(self.sentence)
                              )
                        )
                    )


class ParseTokensOnMorphs:
    def __init__(self, sentence, language="ru_core_news_sm"):
        self.sentence = sentence
        self.nlp = spacy.load(language)

    def action(self):
        return list(
            map(
                lambda a:
                ParseTokenOnMorphs(a).action(),
                filter(
                    lambda a: a.text not in russian_stopwords,
                    self.nlp(self.sentence)
                )
            )
        )


class ParseTokensOnAll:
    def __init__(self, sentence, language="ru_core_news_sm"):
        self.sentence = sentence
        self.nlp = spacy.load(language)

    def action(self):
        return list(
            map(
                lambda a:
                ParseTokenOnAll(a).action(),
                filter(
                    lambda a: a.text not in russian_stopwords,
                    self.nlp(self.sentence)
                )
            )
        )


class ImportWordPairs:
    def __init__(self, sentence, language="ru_core_news_sm"):
        self.nlp = spacy.load(language)
        self.sentence = SplitOnWords(sentence).action()
        self.parsed = displacy.parse_deps(self.nlp(sentence))

    def action(self):
        return list(map(lambda a: tuple([self.sentence[a['start']], self.sentence[a['end']]]), self.parsed["arcs"]))
