import spacy
from nltk.corpus import stopwords
russian_stopwords = stopwords.words("russian")
russian_stopwords.extend(
    ['это', "который", 'он', 'например', 'которые', 'none']
)


class ParseTokensOnTags:
    def __init__(self, sentence, language="ru_core_news_sm"):
        self.sentence = sentence
        self.nlp = spacy.load(language)
        # self.nlp = spacy.blank("ru")

    def action(self):
        return list(map(lambda a: {"text": a.text, "type": a.pos_, "dependence": a.dep_}, self.nlp(self.sentence)))


class ParseTokensOnTags:
    def __init__(self, sentence, language="ru_core_news_sm"):
        self.sentence = sentence
        self.nlp = spacy.load(language)
        # self.nlp = spacy.blank("ru")

    def action(self):
        return list(map(lambda a: {"text": a.text, "type": a.pos_, "dependence": a.dep_}, self.nlp(self.sentence)))


class ParseTokensOnMorphs:
    def __init__(self, sentence, language="ru_core_news_sm"):
        self.sentence = sentence
        self.nlp = spacy.load(language)
        # self.nlp = spacy.blank("ru")

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


class ParseTokenOnMorphs:
    def __init__(self, word):
        self.word = word

    def action(self):
        return dict(
                    list(
                        map(
                            lambda k:
                            tuple(k.split("=")),
                            str(self.word.morph).split("|")
                        )
                    )
                )
            


class ParseTokensOnAll:
    def __init__(self, sentence, language="ru_core_news_sm"):
        self.sentence = sentence
        self.nlp = spacy.load(language)

    def action(self):
        return list(map(lambda a: {**{"text": a.text, "type": a.pos_, "dependence": a.dep_, "morphs": a}, **ParseTokenOnMorphs(a).action()}, self.nlp(self.sentence)))


