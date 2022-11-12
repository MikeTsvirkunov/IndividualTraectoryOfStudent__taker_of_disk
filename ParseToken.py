import spacy
from nltk.corpus import stopwords
russian_stopwords = stopwords.words("russian")
russian_stopwords.extend(
    ['это', "который", 'он', 'например', 'которые', 'none']
)


class ParseTokenOnTags:
    def __init__(self, word):
        self.word = word

    def action(self):
        return {"text": self.word.text, "type": self.word.pos_, "dependence": self.word.dep_}


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
            


class ParseTokenOnAll:
    def __init__(self, word):
        self.word = word

    def action(self):
        return {**ParseTokenOnTags(self.word).action(), **ParseTokenOnMorphs(self.word).action()}


