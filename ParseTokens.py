from ParseToken import *


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
